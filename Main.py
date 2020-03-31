import discord
import config

class MyClient(discord.Client):
    async def on_ready(self):
        print("I just logged in")
        phase = 0

    #wenn nachricht gesendet wird
    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content == "rules":
            await message.channel.send("play a song \n wait \n vote \n hope")
        if message.content.startswith("hello bot"):
            await message.channel.send('Hello, whats up?')
        if message.content.startswith("I vote for"):
            wert_param = -3
            vote = message.content.split(' ')[3]
            await message.channel.send("You voted for " + vote)
            await message.author.send("You got hacked!  you better vote for DuckBoss!")
        if message.content == "Hofmann, we need you!":
            await message.channel.send("Finally happens something")
            await message.channel.send("Well, who ever wants to join the song contest write: I'm in")
            conmem = []                         #Liste von Contest Membern
            phase = 1
        if (phase == 1):
            if message.content == "I'm in":
                conmem.append(message.author)           #Autor zur Liste hinzufügen
                member = str(message.author)            #Autor in einer Stringvariable speichern
                for i in range(1,6):                    #entfernt die Zahlen und das # hinter dem Namen
                    member.pop(-i)
                message.channel.send(member + ", your in")



client = MyClient()
client.run(config.token)
