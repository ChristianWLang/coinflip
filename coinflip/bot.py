import os

import discord


AUTH_TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD_NAME = 'Indecisive'


def register_client():
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=GUILD_NAME)

        print(f'{client.user} has connected to: {guild.name} {guild.id}')
        print(guild.members)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if not '@coinflip' in message.content.lower():
            return

        if '!github' in message.content.lower():
            await message.channel.send(response)


    return client


if __name__ == '__main__':
    client = register_client()
    client.run(AUTH_TOKEN)
