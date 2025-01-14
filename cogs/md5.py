#!/usr/bin/python
# created by : Boulbalah lahcen

from discord.ext import commands
import hashlib

class md5(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def md5(self, ctx, action, *, text):

        # encode md5
        if action == "encode" or action == "e":
            # encode to md5
            output =  hashlib.md5(text.encode()).hexdigest() 
            await ctx.send(output)
            return [output, True]

        # decode md5
        if action == "decode" or action == "d":
            # decode to md5
            if hashlib.md5(text.encode()).hexdigest() == text:
                return [text,True]
            else:
                output = "Eroor"
                return {output,True}

async def setup(client):
    await client.add_cog(md5(client))

