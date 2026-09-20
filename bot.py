import os
import discord
from discord import app_commands

TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = 123456789012345678  # Replace this with YOUR Discord user ID

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set.")

class OwnerOnlyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = OwnerOnlyBot()

def owner_only():
    async def predicate(interaction: discord.Interaction):
        return interaction.user.id == OWNER_ID
    return app_commands.check(predicate)

@bot.tree.command(name="panel", description="Owner-only bot panel")
@owner_only()
async def panel(interaction: discord.Interaction):
    await interaction.response.send_message("This command is owner-only.", ephemeral=True)

@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CheckFailure):
        if interaction.response.is_done():
            await interaction.followup.send("You can't use this bot.", ephemeral=True)
        else:
            await interaction.response.send_message("You can't use this bot.", ephemeral=True)
        return
    raise error

bot.run(TOKEN)
