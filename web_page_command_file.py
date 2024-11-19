import discord
from discord.ui import Button, View


async def web_url(interaction: discord.Interaction):
    try:
        url_embed = discord.Embed(
            title="Welcome to YourSound download!",
            description="Click on the button below to visit the YourSound download site and start downloading your "
                        "favorite tracks using their YouTube url.",
            color=discord.Colour.dark_embed())
        button_url_embed = Button(
            label="YourSound download web site",
            style=discord.ButtonStyle.url,
            emoji="🌐",
            url="https://exemple.com")
        view = View()
        view.add_item(button_url_embed)

        await interaction.response.send_message(embed=url_embed, view=view)
    except Exception as e:
        await interaction.response.send_message(f"Error : {e}")
