# IMPORTS
from discord.ext import commands

from cogs.mor import mor

# INIT CLASS
# should be the same name as the file
class x(commands.Cog):
    def __init__(self, client):
        self.client = client

    # callback to shell showing that the cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        #print('cog name Online')
        print(__file__, ' Online')

    # the actual command
    # x should be the name of the command which should optimally be the same name as the file
    @commands.command()
    async def x(self, ctx, action, *, text):

        # "encode" or "e" entered
        if action == "encode" or action == "e":

            # do the cipher code here

            output = "output of the cipher"
            # this sends the result
            await ctx.send(output)

        # "decode" or "d" entered
        elif action == "decode" or "d":

            # do the cipher code here
           

            output = "output of the cipher"
            # this sends the result
            await ctx.send(output)

# x should be the same name as the init class
async def setup(client):
    await client.add_cog(x(client))