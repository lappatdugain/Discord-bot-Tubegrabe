import logging
import time

import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View

import config
import rules_txt
import welcome_goodbye
import help_command_file
import music_command_file
import web_page_command_file

# Configuration du fichier log
logging.basicConfig(filename='./bot-discord.log',
                    level=logging.INFO)

# Configuration des intents
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix=None, intents=intents)


@bot.event
async def on_ready():
    button = Button(label="I have read and understood the rules",
                    style=discord.ButtonStyle.green,
                    emoji="✅",
                    custom_id="accept_rules_button")

    async def button_callback(interaction: discord.Interaction):
        role = discord.utils.get(interaction.guild.roles, name="member")
        await interaction.user.add_roles(role)
        await interaction.response.send_message("Welcome aboard! By accepting the rules, you’ve unlocked the <@&1101558738818711603> role", ephemeral=True)

    button.callback = button_callback

    view = View(timeout=None)
    view.add_item(button)
    channel = bot.get_channel(1161343187458211923)
    await channel.purge(limit=1)
    await channel.send(rules_txt.rules, view=view)

    print(f'Bot is up')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


welcome_goodbye.welcome(bot)


@bot.event
async def on_message(message):
    logging.info(f'\n Message by : {message.author.name} '
                 f'\n id : ({message.author.id}) '
                 f'\n content : {message.content}'
                 f'\n send : {time.strftime("%A %d %B %Y %H:%M:%S")}')


@bot.tree.command(name="ping", description="command ping")
async def ping(interaction: discord.Integration):
    await interaction.response.send_message("Pong")


@bot.tree.command(name="help", description="Commands list")
async def help(interaction: discord.Integration):
    await help_command_file.help_command(interaction)


@bot.tree.command(name="music", description="Download youtube mp3 with url")
@app_commands.describe(url="url youtube")
async def music(interaction: discord.Integration, url: str):
    await music_command_file.music_command(interaction, url)


@bot.tree.command(name="website", description="link to website")
async def website(interaction: discord.Integration):
    await web_page_command_file.web_url(interaction)


# Run the bot

bot.run(config.token())
