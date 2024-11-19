import discord


async def help_command(interaction: discord.Interaction):
    try:
        embed = discord.Embed(title=f"Commands list",
                              description="- `/ping` : Use to ping bot"
                                          "\n- `/music` : Download youtube mp3 with url"
                                          "\n- `/website` : Provides a link to the YouSound download website for "
                                          "downloading YouTube videos in MP3 or MP4 format.",
                              colour=discord.Colour.yellow())
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")
