import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default();
intents.message_content = True;

bot = commands.Bot(command_prefix='?', intents=intents);

# Log

async def log_use(ctx, *args) -> int:
    x = datetime.now()
    print(f"Log_command: {ctx.author} used command: {ctx.command}. Arguments: {args}. Log generated: {x.strftime("%d/%m/%Y %H:%M:%S")}.");
    return 1;

# Commands

@bot.command()
async def hey(ctx, *args) -> None:
    if await log_use(ctx, args):
        await ctx.send(f"Hey {ctx.author.mention}! How are ya?", mention_author=True);

# Misc

def readToken(path : str) -> str:
    with open(path, "r") as f:
        ctx = f.read();
        return ctx;

# Run

bot.run(readToken("token.txt"));
