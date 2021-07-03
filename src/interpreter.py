#!/usr/bin/env python

import os
import ast
import re
import multiprocess
from pathos.multiprocessing import ProcessPool

import dotenv
import discord
from discord.ext import commands
import RestrictedPython
from RestrictedPython import compile_restricted, utility_builtins
from RestrictedPython.PrintCollector import PrintCollector

dotenv.load_dotenv()

def interpret(code):
    code += "\nresults = printed"
    byte_code = compile_restricted(
        code,
        filename = "<string>",
        mode = "exec",
    )
    data = { 
        "_print_"      : PrintCollector,
        "__builtins__" : {
            **utility_builtins,
            "all"                   : all,
            "any"                   : any,
            "_getiter_"             : RestrictedPython.Eval.default_guarded_getiter,
            "_iter_unpack_sequence_": RestrictedPython.Guards.guarded_iter_unpack_sequence
        },
        "_getattr_": RestrictedPython.Guards.safer_getattr
    }
    
    exec(byte_code, data, None)
    return data["results"]