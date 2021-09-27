#!/usr/bin/env python

import os
import re

from discord.ext import commands

from python_commands import PythonCog
from jokes_commands import JokesCog

Bot = commands.Bot(command_prefix = '!') # prefix

@Bot.command(name = 'ping') # verifies that the bot is running
async def ping(ctx): 
    await ctx.send("pong!") 


Bot.add_cog(PythonCog(Bot))

Bot.add_cog(JokesCog(Bot))


if __name__ == '__main__':
    print('Bot Corriendo!')
    Bot.run("ODYwNTcyNzM3MjAyMjkwNzU5.YN9M0Q.9txucxA2EgstI-P1WiUODksjcrA")