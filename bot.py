import os
import discord
from discord import app_commands

TOKEN = os.getenv("DISCORD_TOKEN")

# YOUR Discord User ID
OWNER_ID = 1373549788628254821

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set.")

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = MyBot()


def owner_only():
    async def check(interaction: discord.Interaction):
        return interaction.user.id == OWNER_ID

    return app_commands.check(check)


@bot.tree.command(name="panel", description="Owner-only panel")
@owner_only()
async def panel(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Welcome, owner!",
        ephemeral=True
    )


@bot.tree.error
async def command_error(
    interaction: discord.Interaction,
    error: app_commands.AppCommandError
):
    if isinstance(error, app_commands.CheckFailure):
        await interaction.response.send_message(
            "You can't use this bot.",
            ephemeral=True
        )


bot.run(TOKEN)
