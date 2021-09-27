#!/usr/bin/env python

import os
import re

from discord.ext import commands

from python_commands import PythonCog

Bot = commands.Bot(command_prefix = '!') # prefix

@Bot.command(name = 'ping') # verifies that the bot is running
async def ping(ctx): 
    await ctx.send("pong!") 


Bot.add_cog(PythonCog(Bot))


if __name__ == '__main__':
    print('Bot Corriendo!')
    Bot.run(os.getenv("TOKEN"))