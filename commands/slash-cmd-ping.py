import disnake
from disnake.ext import commands

from dotenv import load_dotenv
load_dotenv()

import os, random, asyncio

class PingCommand(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.slash_command(
        name="ping",
        description="Returns websocket latency.",
    )
    async def ping(self, ctx):
        await ctx.response.send_message(f"<:weird:925717694723002388> `{round(self.client.latency * 1000)}ms`")

def setup(client):
    client.add_cog(PingCommand(client))