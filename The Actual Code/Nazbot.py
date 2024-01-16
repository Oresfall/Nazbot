# Planning some Features before actually code it
# Plans:
#   1. Adding commands that send nazrin fan art from Reddit
#   2. Nazrin trivias would be funny
#   3. Cheese images for no reason
#   
#   

import discord
from discord.ext import commands

client = commands.Bot(command_prefix="n!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Cheesed to meet you devs!")
    print("--------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Cheesed to meet you, im Nazbot!")

client.run('xxx')

if __name__ == '__main__':
    print("nazrin!")