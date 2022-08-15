import commands
from configparser import ConfigParser


config_object = ConfigParser()

config_object["admins"] = {
    "admin1": "ADMIN1",
    "admin2": "ADMIN2",
    "admin3": "ADMIN3",
    "admin4": "ADMIIN4"
}

config_object["values"] = {
    "startmoney": "1000"

}

with open('config.ini', 'w') as conf:
    config_object.write(conf)


commands.start()


