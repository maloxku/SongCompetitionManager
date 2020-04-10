import discord
import config

class MyClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.phase = 0
        #Liste von Contest Membern
        self.conmem = []

    async def on_ready(self):
        print("I just logged in")
        phase = 0

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content == "rules":
            await message.channel.send("play a song \n wait \n vote \n hope")
        if message.content == "Click here to get in:":
            await message.add_reaction("💩")
            self.conmem.clear()
            self.phase = 1
    async def on_reaction_add(self, reaction, user):
        if (user == client.user):
            return
        await reaction.message.channel.send(str(user.mention) + ', your in')
        self.conmem.append(user)



client = MyClient()
client.run(config.token)