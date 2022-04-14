import commands
from configparser import ConfigParser


config_object = ConfigParser()

config_object["admins"] = {
    "admin1": "Danny3000®#3854",
    "admin2": "!!!!Horizon_gaming!!!!#2245",
    "admin3": "MyGame TV#5403",
    "admin4": "dexder123#8153"
}

config_object["values"] = {
    "startmoney": "1000"

}

with open('config.ini', 'w') as conf:
    config_object.write(conf)


commands.start()


