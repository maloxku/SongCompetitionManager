import discord
import config

class MyClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.phase = 0
        #Liste von Contest Membern
        self.conmem = []
        # id der aktuellen Nachricht zum Beitreten des Events
        self.join_message_id = None

    async def on_ready(self):
        print("I just logged in")

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content == "rules":
            await message.channel.send("play a song \n wait \n vote \n hope")
        if message.content == "Click here to get in:":
            self.join_message_id = message.id
            await message.add_reaction("💩")
            self.conmem.clear()
            self.phase = 1

    async def on_reaction_add(self, reaction, user):
        if (user == client.user):
            return
        # Überprüfen, ob die Nachricht auf die reagiert wird auch die join-message ist:
        if reaction.message.id == self.join_message_id:
            await reaction.message.channel.send(str(user.mention) + ', you\'re in')
            self.conmem.append(user)

    async def on_reaction_remove(self, reaction, user):
        if reaction.message.id == self.join_message_id:
            await reaction.message.channel.send(str(user.mention) + ', you\'re out')
            if user in self.conmem:
                self.conmem.remove(user)



client = MyClient()
client.run(config.token)
