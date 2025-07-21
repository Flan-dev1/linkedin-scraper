import linkedin
import discord
from discord.ext import commands 
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@commands.command()
async def test(ctx):
    jobslist = linkedin.getJobsList()
    await ctx.send(jobslist)

bot.add_command(test)    

bot.run(token)