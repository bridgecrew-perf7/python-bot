#!/usr/bin/env python

import os
import multiprocess
from pathos.multiprocessing import ProcessPool
import random

from discord.ext import commands

from interpreter import interpret

bot = commands.Bot(command_prefix = '!') # prefix

@bot.command(name = 'ping') # verifies that the bot is running
async def ping(ctx): 
    await ctx.send("pong!") 


@bot.command(name = 'py') # interpret python code and return the output
async def debug(ctx, *, message):
    if '```python' in message: # remove discord decorator
        message = message[9:]
        message = message[:-3]
    
    pool = ProcessPool(nodes = 4)
    debug = pool.apipe(interpret,message)

    try:
        output = debug.get(timeout = 7)

    except multiprocess.context.TimeoutError: # timeout error
        output = "`Se excedió el tiempo de ejecución :(`"

    except Exception as error_name: # syntax error or not implemented functionality
        output = f"`Error: {error_name}`"

    await ctx.send(output)


@bot.command(name = 'meme') # returns a random meme (img)
async def meme(ctx): 
    memes = [
        'https://img.devrant.com/devrant/rant/r_2222259_ab3At.jpg',
        'https://img.devrant.com/devrant/rant/r_3845088_HgBjZ.jpg',
        'https://forum.onefourthlabs.com/uploads/default/original/1X/e16be32056974b4ccfa5c6f7300c8c36f97cdeb3.jpeg',
        'https://pics.me.me/when-you-write-i-in-a-python-code-we-dont-63760085.png',
        'https://miro.medium.com/max/572/1*-81rUyhT8snH86Lfet6jNA.jpeg',
        'https://pics.me.me/thumb_when-your-code-is-a-mess-but-it-still-works-71570634.png',
        'http://images7.memedroid.com/images/UPLOADED915/5b606b55be7f9.jpeg'
    ] #memelist
    response = random.choice(memes)
    await ctx.send(response)


if __name__ == '__main__':
    print('Bot Corriendo!')
    bot.run(os.getenv("TOKEN"))