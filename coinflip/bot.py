import os
import random

import discord
from discord.ext import commands


AUTH_TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD_NAME = 'Indecisive'


def when_mentioned_exclamation(bot, message):
    prefixes = commands.when_mentioned(bot, message)
    return [p + '!' for p in prefixes]


def register_client():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=when_mentioned_exclamation, intents=intents)

    @bot.command(name='github', help='This bot\'s github, where you can contribute')
    async def _github(ctx):
        await ctx.send('https://github.com/ChristianWLang/coinflip')

    @bot.command(name='flip', help='Flip a coin')
    async def _github(ctx):
        await ctx.send(random.choice(['Heads!', 'Tails!']))

    @bot.command(name='randint', help='Random integer between two numbers, inclusive')
    async def _github(ctx, lower: int, upper: int):
        await ctx.send(f'{random.randint(lower, upper)}')

    @bot.event
    async def on_ready():
        guild = discord.utils.get(bot.guilds, name=GUILD_NAME)

        print(f'{bot.user} has connected to: {guild.name} {guild.id}')
        print(guild.members)

    return bot


if __name__ == '__main__':
    bot = register_client()
    bot.run(AUTH_TOKEN)
