#!/usr/bin/env python
import os
import ast
import re
import multiprocess
from pathos.multiprocessing import ProcessPool
import random

from interpreter import interpret

from discord.ext import commands

bot = commands.Bot(command_prefix = '!') # prefix

@bot.command(name = 'ping')
async def randomMeme(ctx): # verify that the bot is running
    await ctx.send("pong!") 


@bot.command(name = 'py')
async def debug(ctx, *, message):
    if '```python' in message:
        message = message[9:]
        message = message[:-3]
    
    pool = ProcessPool(nodes = 4)
    debug = pool.apipe(interpret,message)

    try:
        output = debug.get(timeout = 7)

    except multiprocess.context.TimeoutError: # se excedió tiempo de respuesta
        output = "ERROR -se excedió el tiempo de ejecución"

    except: # error de sintaxis
        output = "ERROR -No pude interpretar el código, por favor, revisa si hay algún error de sintaxis"

    await ctx.send(output)


@bot.command(name = 'meme')
async def randomMeme(ctx): # Función que devuelve un meme (img) aleatorio
    memes = [
        'https://img.devrant.com/devrant/rant/r_2222259_ab3At.jpg',
        'https://img.devrant.com/devrant/rant/r_3845088_HgBjZ.jpg',
        'https://forum.onefourthlabs.com/uploads/default/original/1X/e16be32056974b4ccfa5c6f7300c8c36f97cdeb3.jpeg',
        'https://pics.me.me/when-you-write-i-in-a-python-code-we-dont-63760085.png',
        'https://miro.medium.com/max/572/1*-81rUyhT8snH86Lfet6jNA.jpeg',
        'https://pics.me.me/thumb_when-your-code-is-a-mess-but-it-still-works-71570634.png',
        'https://vincentdnl.com/static/53be1c651fa390e15b1ba2dc146231b4/5f4af/semicolon.png',
        'http://images7.memedroid.com/images/UPLOADED915/5b606b55be7f9.jpeg'
    ] #memelist
    response = random.choice(memes)
    await ctx.send(response)


if __name__ == '__main__':
    print('Bot Corriendo!')
    bot.run(os.getenv("TOKEN"))