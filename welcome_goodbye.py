import discord
from discord.ext import commands


def welcome(bot):
    @bot.event
    async def on_member_join(member):
        guild = member.guild
        channel = guild.system_channel
        if channel is not None:
            message = f"Welcome {member.mention} to the {guild.name} server !"
            await channel.send(message)

    @bot.event
    async def on_member_remove(member):
        guild = member.guild
        channel = guild.system_channel
        if channel is not None:
            message = f"Bye {member.mention}  see you soon on the {guild.name} server !"
            await channel.send(message)
