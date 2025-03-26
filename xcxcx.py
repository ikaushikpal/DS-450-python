import discord
import os
import alive
from my_logger import my_logger
from dotenv import load_dotenv
from replit import db

load_dotenv()
client = discord.Client()
logger = my_logger()


@client.event
async def on_ready():
    logger.debug(f"logged as {client.user} and bot is online")


def print_help():
    message = f"{'='*78}\nWelcome to help section of this JOKE bot.\n\nThere are 6 different category available, i.e.\nany, misc, programming, dark, pun, spooky and christmas\n\nFor example if you write \n!joke dark then BOT will display any dark joke available on internet\n{'='*78}"
    return message


@client.event
async def on_message(message):

    if message.author == client.user:
        logger.info(f"Bot wrote {message.content}")

    elif message.content == '$meet help':
        await message.channel.send(print_help())

    elif message.content == '$meet':
        authorName = f'{message.author}'
        url = 'Null'
        if authorName in db.keys():
            url = db[authorName]

        embed = discord.Embed(
            title="Google Meet Url",
            description="Joining link for meet",
            color=0xFF5733)
        embed.set_author(name=message.author.display_name,
                         icon_url=message.author.avatar_url)
        embed.add_field(name="link", value=url, inline=False)
        channel = client.get(969828494848720946)
        return await channel.send(embed=embed)

    elif message.content.startswith('$meet set'):
        meetURL = message.content[10:]
        authorName = f'{message.author}'
        db[authorName] = meetURL

        embed = discord.Embed(
            title="Successfully Updated GMeet URL",
            color=0xFF5733)
        embed.set_author(name=message.author.display_name,
                            icon_url=message.author.avatar_url)
        channel = client.get(969828494848720946)
        return await channel.send(embed=embed)


if __name__ == "__main__":
    logger.debug("PROGRAM STARTED")
    alive.alive()
    client.run(os.getenv('TOKEN'))
