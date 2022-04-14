from configparser import ConfigParser
import os.path


def read_money(user):
    if os.path.exists("users/" + str(user) + '.ini'):
        config_user = ConfigParser()
        config_user.read("users/" + str(user) + ".ini")

        money = config_user["USERINFO"]
        money = money["money"]

        return "Du hast " + money + "$"
    else:
        return "Du hast noch keinen Account, bitte erstelle dir einen mit !createme"


