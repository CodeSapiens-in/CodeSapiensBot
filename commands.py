import os

from dotenv import load_dotenv

import discord 
from discord import app_commands
import sheets


MY_GUILD = discord.Object(id=1160074434988753008)

load_dotenv()
class Client(discord.Client):
    
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    


    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)
    
   
    # Command implementation. Is tested and will work when slash commands work.


client = Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')



@client.tree.command(name='register', description='Register yourself to our community')
@app_commands.describe(department='Short form of your department e.g. CSE,IT, AIDS, ECE')
@app_commands.describe(passout_year='Year of passout 2024,2025 etc.')
@app_commands.describe(college='College name')
async def register(interaction: discord.Interaction,department: str,passout_year:int,college:str):
   # Write code to update google spreadsheets
   try:
    print(department,str(passout_year),college)
    await interaction.response.defer(ephemeral=True)
    await sheets.add_user(interaction.user.name,passout_year,department,college)
    await interaction.followup.send(f'Thanks for Registering',ephemeral=True)
   except Exception as e: print(e)


BOT_TOKEN=os.getenv('BOT_TOKEN')
client.run(BOT_TOKEN)
