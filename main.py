import disnake
from disnake.ext import commands

from dotenv import load_dotenv
load_dotenv()

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

client.loadedcogs = []
client.unloadedcogs = []

@client.event
async def on_ready():

    await client.change_presence(
        status=disnake.Status.idle,
        activity=disnake.Activity(
            type=disnake.ActivityType.watching, name="the world burn."
        ),
    )

    print("---------- COMMANDS ----------")
    for filename in os.listdir("./commands"):
        try:
            if filename.endswith(".py"):
                client.load_extension(f"commands.{filename[:-3]}")
                client.loadedcogs.append(filename[:-3])
                print(f"|  Loaded {filename}.")
            else:
                pass
        except Exception as e:
            print(f"|  Could not load {filename} due to exception: \n{e}")

    print("----------- EVENTS -----------")
    for filename in os.listdir("./events"):
        try:
            if filename.endswith(".py"):
                client.load_extension(f"events.{filename[:-3]}")
                client.loadedcogs.append(filename[:-3])
                print(f"|  Loaded {filename}.")
            else:
                pass
        except Exception as e:
            print(f"|  Could not load {filename} due to exception: \n{e}")
    
    print("------------------------------")
    print(f"|  Logged in as {client.user}.")

@client.slash_command(
    name="weird",
    description="A random weird thing.",
)
async def weird(ctx):
    await ctx.response.send_message("<:weird:925717694723002388>")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
client.run(BOT_TOKEN)