from configparser import ConfigParser
import os.path

config_object = ConfigParser()

def money(id2):
    if os.path.exists("users/" + id2 + ".ini"):
        config_object.read("users/" + id2 + ".ini")
        userinfo = config_object["USERINFO"]
        return userinfo["money"]
    else:
        return False

def name(id):
    if os.path.exists("users/" + id + ".ini"):
        config_object.read("users/" + id + ".ini")
        userinfo = config_object["USERINFO"]
        return userinfo["username"]
    else:
        return False

def admin(person2):
    person = str(person2)
    if person.find("#") == -1:
        person = name(person)

    config_object.read("config.ini")
    admin = config_object["admins"]

    temp = False
    count = True
    num = 1
    while count:
        try:
            temp2 = admin["admin" + str(num)]
        except:
            count = False
        else:
            num += 1

        if person == temp2:
            temp = True

    return temp

def mopc(messagecontent):
    user = messagecontent
    user = str(user)
    if not user.find("!") == -1:
        temp = 3
    else:
        temp = 2

    user = user[temp:]
    user = user[:-1]

    return str(user)