from configparser import ConfigParser
import os.path

config_user = ConfigParser()

def profilep(id, url):
    if not os.path.exists("users/" + str(id) + '.ini'):
        return "Du hast keinen Account!"

    config_user.read("users/" + str(id) + '.ini')
    userinfo = config_user["USERINFO"]
    userinfo["picture"] = str(url)

    with open("users/" + str(id) + '.ini', 'w') as conf:
        config_user.write(conf)

    return "Dein Profilbild wurde aktualisirt!"