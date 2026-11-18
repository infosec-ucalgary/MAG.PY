import discord
from discord import app_commands
from discord.ext import commands


class Musician(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="queue",
        description="Show the music queue and controls"
    )

    @app_commands.guild_only()
    async def queue(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Music queue",
            description="No song is playing.",
            color=discord.Color.purple()
        )
        embed.add_field(
            name="Up next",
            value="The queue is empty.",
            inline=False
        )

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Musician(bot))