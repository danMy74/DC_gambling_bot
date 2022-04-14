from configparser import ConfigParser
import os.path

config_user = ConfigParser()
config_object = ConfigParser()

config_object.read("config.ini")


def creatme2(user, username, avatar):
    if os.path.exists("users/" + str(user) + '.ini'):
        return "Du hast bereits einen Account"
    else:

        startmoney = config_object["values"]
        startmoney = startmoney["startmoney"]

        config_user["USERINFO"] = {
            "name": user,
            "money": startmoney,
            "username": username,
            "picture": avatar
        }

        with open("users/" + str(user) + '.ini', 'w') as conf:
            config_user.write(conf)


    return "Account erstellt"




