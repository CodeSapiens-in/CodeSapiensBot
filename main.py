# This example requires the 'members' privileged intent to function.

import discord
from dotenv import load_dotenv
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('test'):
            await message.reply('Test success', mention_author=True)


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

load_dotenv()

BOT_TOKEN=os.getenv('BOT_TOKEN')
client = MyClient(intents=intents)
client.run(BOT_TOKEN)