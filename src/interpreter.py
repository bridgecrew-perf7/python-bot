#!/usr/bin/env python

import os
import multiprocess
from pathos.multiprocessing import ProcessPool

import dotenv
import discord
from discord.ext import commands
import RestrictedPython
from RestrictedPython import compile_restricted, utility_builtins
from RestrictedPython.PrintCollector import PrintCollector

import numpy as np
import random

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
            "_getitem_"             : RestrictedPython.Eval.default_guarded_getitem,
            "_unpack_sequence_"     : RestrictedPython.Guards.guarded_iter_unpack_sequence,
            "_iter_unpack_sequence_": RestrictedPython.Guards.guarded_iter_unpack_sequence,
            "len"                   : len,
            "list"                  : list,
            "range"                 : range,
            "abs"                   : abs,
            "dict"                  : dict,
            "str"                   : str,
            "int"                   : int,
            "max"                   : max,
            "round"                 : round,
            "map"                   : map,
            "np"                    : np,
            "random"                : random,
            "ascii"                 : ascii,
            "bool"                  : bool,
            "bytearray"             : bytearray,
            "bytes"                 : bytes,
            "eval"                  : eval,
            "exec"                  : exec,
            "filter"                : filter,
            "float"                 : float,
            "format"                : format,
            "hash"                  : hash,
            "id"                    : id,
            "iter"                  : iter,
            "locals"                : locals,
            "min"                   : min,
            "ord"                   : ord,
            "pow"                   : pow,
            "repr"                  : repr,
            "reversed"              : reversed,
            "sum"                   : sum,
            "set"                   : set,
            "sorted"                : sorted

        },
        "_getattr_": RestrictedPython.Guards.safer_getattr
    }
    
    exec(byte_code, data, None)
    return data["results"]