import disnake
from disnake.ext import commands

import os, random, asyncio

bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents().all(),
    test_guilds=[
        int(os.environ.get("MAIN_GUILD")),
        int(os.environ.get("TEST_GUILD")),
    ],
    help_command=None,
)

@bot.event
async def on_ready():
    print("The bot is now online. :weird:")


@bot.command()
async def test(ctx):
    await ctx.reply("I truly do exist <:weird:925717694723002388>")

@bot.slash_command(description="slash test")
async def slash_test(ctx):
    await ctx.response.send_message("This slash command truly works <:weird:925717694723002388>")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot.run(BOT_TOKEN)