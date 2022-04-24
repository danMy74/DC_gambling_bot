import discord
from command import createme, money_state, money, profil, profile_picture, blackjeck, delu
import functions
from dotenv import dotenv_values

dotenv = dotenv_values("data.env")
TOKEN = dotenv["TOKEN"]

def start():
    class luck(discord.Client):

        async def on_ready(self):
            print("logged in...")
            print("wait for messages...")

        # nachrichten eingang
        async def on_message(self, message):

            if message.author == client.user:  # not accept bot messages
                return
            if str(message.channel.type) == "private":  # not accept privat messages
                return



            # command
            if message.content.startswith("!createme"):
                await message.channel.send(createme.creatme2(message.author.id, message.author, message.author.avatar_url))

            if message.content.startswith("!moneystate"):
                await message.channel.send(money_state.read_money(message.author.id))

            if message.content.startswith("!money "): #add, set, remove, clear ToDo: worter als werte vermeiden (try)
                if functions.admin(message.author):
                    await message.channel.send(money.money(message.content[7:]))
                else:
                    await message.channel.send("Du hast keine Berechtigungen dafür!")

            if message.content.startswith("!profil "):
                await message.channel.send(embed= profil.profil(message.content[8:]))

            if message.content.startswith("!update profil picture"):
                await message.channel.send(profile_picture.profilep(message.author.id, message.author.avatar_url))

            if message.content.startswith("!invite"):
                await message.channel.send("INSERT INVITE LINK HERE")

            if message.content.startswith("!blackjack "):
                await message.channel.send(blackjeck.black_jack(message.content[11:]), message.author.id)

            if message.content.startswith("!del "):
                if functions.admin(message.author):
                    await message.channel.send(delu.delu(message.content[5:]))
                else:
                    await message.channel.send("Du hast keine Berechtigungen dafür!")








    client = luck()
    client.run(TOKEN)
