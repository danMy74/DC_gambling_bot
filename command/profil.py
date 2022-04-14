import discord
import os.path
from configparser import ConfigParser
import functions

config_object = ConfigParser()

def profil(person):
    if not person.find("!") == -1:
        temp = 3
    else:
        temp = 2

    person = person[temp:]
    person = person[:-1]

    if not os.path.exists("users/" + str(person) + '.ini'):

        not_found = discord.Embed(
            colour=discord.Colour.dark_red(),
        )

        not_found.set_footer(text="by luckybot")
        not_found.set_author(name="Profil not found")

        return not_found

    config_object.read("users/" + str(person) + '.ini')
    avatar = config_object["USERINFO"]
    avatar = str(avatar["picture"])

    name = functions.name(person)



    embed = discord.Embed(
        colour= discord.Colour.dark_red(),
    )

    embed.set_footer(text= "by luckybot")
    embed.set_thumbnail(url= avatar)
    embed.set_author(name= "Profil of: " + str(name), icon_url= str(avatar))
    embed.add_field(name= "Money:", value= functions.money(person) + "$", inline= False)


    return embed

#ToDo: Design des embeds anpassen und befhele zum gestalten des Profiles festlegen, Kontostand muss rein. Video: https://www.youtube.com/watch?v=XKQWxAaRgG0, es muss einen befhel geben das profilbild upzudaten einfach in der user config die url erneuern