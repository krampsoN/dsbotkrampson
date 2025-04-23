import discord
from discord.ext import commands
import os
import sys

intents = discord.Intents.default()
intents.message_content = True  # ОБЯЗАТЕЛЬНО!

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Бот запущен как {bot.user}")

@bot.command()
async def привет(ctx):
    await ctx.send("Привет! Я всегда онлайн на Railway!")

token = os.getenv("DISCORD_TOKEN")
if not token:
    print("❌ Переменная окружения DISCORD_TOKEN не найдена. Завершаем.")
    sys.exit(1)

bot.run(token)
