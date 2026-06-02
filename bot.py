import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default();
intents.message_content = True;

bot = commands.Bot(command_prefix='?', intents=intents);

bot_owner : int = 701431218490703952;

# Error

err = {
    0 : 0, # count
    1 : "Log Failed.",
    2 : "Invalid user.",
    3 : "Invalid permissions.",
    4 : "Internal method faliure.",

    99 : "Test",
    100 : "Couldn't evaluate the given command."
};

class Error:
    def __init__(self, ctx : dict,level : int, e : int):
        self.level = level;
        self.ctx = ctx;
        self.e = e + 1;
    async def log_error(self) -> int:
        x = datetime.now();
        y = x.strftime("%d/%m/%Y %H:%M:%S");
        print(f"Error_{self.e}: {self.ctx.author} at {y} used {self.ctx.command}. ec_{self.level}: {err[self.level]}.");

# Log

async def log_use(ctx, *args) -> int:
    x = datetime.now()
    print(f"Log_command: {ctx.author} used command: {ctx.command}. Arguments: {args}. Log generated: {x.strftime("%d/%m/%Y %H:%M:%S")}.");
    return 1;

async def throw_error(ctx : dict = {}, args : tuple = (), errorLevel : int = 99) -> int:
    tmp = Error(ctx, errorLevel, err[0]);
    err[0] = tmp.e;
    await tmp.log_error();
    return 0;

async def toggle_verbose(ctx : dict, args : tuple) -> int :
    print(f"-v : {verb}.");
    print(f"{args}, len {len(args)}");
    return 0;


# Evals



eva = {
    'throw_error' : throw_error,
    'verbose' : toggle_verbose
}

# Commands

@bot.command()
async def hey(ctx, *args) -> None:
    if await log_use(ctx, args):
        await ctx.send(f"Hey {ctx.author.mention}! How are ya?", mention_author=True);
    else:
        await throw_error(ctx, args, 1);

@bot.command()
async def eval(ctx, *args) -> None:
    if await log_use(ctx, args):
        if ctx.author.id == bot_owner:
            print(f"{args[0]}");
        else:
            await throw_error(ctx, args, 3);
    else:
        await throw_error(ctx, args, 1);

# Misc

def readToken(path : str) -> str:
    with open(path, "r") as f:
        ctx = f.read();
        return ctx;

# Run

bot.run(readToken("token.txt"));
