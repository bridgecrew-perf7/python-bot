#!/usr/bin/env python

import discord
from discord.ext import commands

import random

class JokesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ['meme'])
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
    

    @commands.command(aliases = ['nashe', 'ashe'])
    async def nonsense(ctx):
        output = ':smirk::hamburguer:'
        await ctx.send(output)