import disnake
from disnake.ext import commands

import os, random, asyncio

client = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents().all(),
    test_guilds=[
        int(os.environ.get("MAIN_GUILD")),
        int(os.environ.get("TEST_GUILD")),
    ],
    help_command=None,
)

@client.event
async def on_ready():
    print("The bot is now online. :weird:")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot.run(BOT_TOKEN)