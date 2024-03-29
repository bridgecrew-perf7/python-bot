#!/usr/bin/env python

import re
from inplace import protected_inplacevar
from discord.ext import commands
import multiprocess
import RestrictedPython
from pathos.multiprocessing import ProcessPool
from RestrictedPython.PrintCollector import PrintCollector
from RestrictedPython import compile_restricted, utility_builtins

class PythonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["py", "python", "python3"])
    async def debug(self, ctx, *, message):
        # Remove discord decorator, '`' character and os import for security
        message = re.sub("|\```python|\`|import os|```py","",message)

        pool = ProcessPool(nodes = 4) 
        debug = pool.apipe(interpret,message)

        try: # 7 seconds timeout predefined
            output = debug.get(timeout = 7)

        except multiprocess.context.TimeoutError: # Timeout error
            output = "`Se excedió el tiempo de ejecución :(`"

        except Exception as error_name:  # Syntax error or not implemented functionality
            output = f"`Error: {error_name}`"

        await ctx.send(output)


def interpret(code):
    #  Necessary to show output, save in data ['results'] the prints of the execution
    code += "\nresults = printed" 

    #  Interpreter, mode exec to be able to use statements, methods, classes, functions, etc.
    byte_code = compile_restricted(
        code,
        filename = "<string>",
        mode = "exec",
    )
    #  All the functionalities available to the bot are stored in data, mostly builtins
    data = {
        "_print_"      : PrintCollector,
        "getattr"      : getattr,
        "__builtins__" : {
            **utility_builtins,
            "__import__"            : __import__,
            "_inplacevar_"          : protected_inplacevar,
            "all"                   : all,
            "any"                   : any,
            "_getiter_"             : RestrictedPython.Eval.default_guarded_getiter,        # iteraciones en bucles
            "_getitem_"             : RestrictedPython.Eval.default_guarded_getitem,        # acceder a un valor de una lista por su indice
            "_getattr_"               : getattr,
            "_unpack_sequence_"     : RestrictedPython.Guards.guarded_iter_unpack_sequence, 
            "_iter_unpack_sequence_": RestrictedPython.Guards.guarded_iter_unpack_sequence,
            "slice"                 : slice,
            "round"                 : round,
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
            "sorted"                : sorted,
            "next"                  : next,
        },
        "_getattr_": RestrictedPython.Guards.safer_getattr
    }

    exec(byte_code, data, None) #  Get the output
    return data["results"] #  data["results"] only contains prints or NameErrors if exists
