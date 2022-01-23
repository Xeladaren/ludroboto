#!/bin/python3

import discord
import setting

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_guild_join(self, guild):
        print("Bot join {0}!".format(guild.name))

    async def on_guild_remove(self, guild):
        print("Bot remove {0}!".format(guild.name))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))

        if self.user in message.mentions:
            print("ping")
            await message.reply("Saluton !", mention_author=False)


client = MyClient()
client.run(setting.botToken)


print("Saluton mondo.")
