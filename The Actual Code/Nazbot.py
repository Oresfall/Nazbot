# Planning some Features before actually code it
# Plans:
#   1. Adding commands that send nazrin fan art from Reddit
#   2. Nazrin trivias would be funny, either cheese trivias or mouse trivias or just simply Touhou
#   3. Cheese images for no reason
#   4. Favorite daily cheese chosen random everyday
#   5. 

import discord
from discord.ext import commands
from apikeys import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="n!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Cheesed to meet you devs!")
    print("--------------------------")


#On member joining, remove brackets to make it work (i still cant make a manual command to turn it off!!!!)
#@client.event
#async def on_member_join(member):
#   channel = client.get_channel(Channel ID here)
#   await channel.send("Welcome! Don't forget to read the rules!")
#   await member.send("Welcome to the server!")
  

# Below are all commands listed available for members to use
@client.command()
async def hello(ctx):
    await ctx.send("Cheesed to meet you, im Nazbot!")

@client.command()
async def trivia(ctx):
    await ctx.send("Squeeks! Looks like I haven't thought of any trivia, please wait soon!")

# Dont forget to put your bot token in apikeys.py
client.run(BOTTOKEN)

if __name__ == '__main__':
    print("nazrin!")