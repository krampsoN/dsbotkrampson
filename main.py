
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Бот запущен как {bot.user}")

@bot.command()
async def привет(ctx):
    await ctx.send("Привет! Я всегда онлайн на Railway!")

bot.run(os.environ["DISCORD_TOKEN"])
