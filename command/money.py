from configparser import ConfigParser
import functions
import os.path

def money(kind):




    def edit(user, type, mount = ""):
        config_object = ConfigParser()
        if type == "add":
            config_object.read("users/" + str(user) + '.ini')
            userinfo = config_object["USERINFO"]
            userinfo["money"] = str(int(userinfo["money"]) + int(mount))
            with open("users/" + str(user) + '.ini', 'w') as conf:
                config_object.write(conf)
            return str(mount) + "$ added to user: " + functions.name(user)


        elif type == "remove":
            config_object.read("users/" + str(user) + '.ini')
            userinfo = config_object["USERINFO"]
            userinfo["money"] = str(int(userinfo["money"]) - int(mount))
            with open("users/" + str(user) + '.ini', 'w') as conf:
                config_object.write(conf)
            return str(mount) + "$ removed from user: " + functions.name(user)

        elif type == "clear":
            config_object.read("users/" + str(user) + '.ini')
            userinfo = config_object["USERINFO"]
            userinfo["money"] = "0"
            with open("users/" + str(user) + '.ini', 'w') as conf:
                config_object.write(conf)
            return "Money of user: " + functions.name(user) + " was cleared"

        elif type == "set":
            config_object.read("users/" + str(user) + '.ini')
            userinfo = config_object["USERINFO"]
            userinfo["money"] = str(mount)
            with open("users/" + str(user) + '.ini', 'w') as conf:
                config_object.write(conf)
            return "Money of user: " + functions.name(user) + " set to: " + mount


    if kind.find("add") == 0: #bei add befehl
        if not kind.find("!") == -1:
            temp = 3
        else:
            temp = 2

        name_start = kind[4:]
        name_end = name_start.find(" ")
        name = name_start[:name_end]

        money_start = name_start[name_end +1:]
        money_end = money_start.find(" ")

        user = name[temp:]
        user = user[:-1]

        if not os.path.exists("users/" + str(user) + '.ini'):
            return "Diese Person hat noch keinen Account!"
        else:
            if name == "" or money_end != -1 or name_end == -1:
                return "Type Error in command"
            else:
                return edit(user, "add", money_start)



    elif kind.find("remove") == 0: # bei remove befehl
        if not kind.find("!") == -1:
            temp = 3
        else:
            temp = 2

        name_start = kind[7:]
        name_end = name_start.find(" ")
        name = name_start[:name_end]

        money_start = name_start[name_end + 1:]
        money_end = money_start.find(" ")

        user = name[temp:]
        user = user[:-1]

        if not os.path.exists("users/" + str(user) + '.ini'):
            return "Diese Person hat noch keinen Account!"
        else:
            if name == "" or money_end != -1 or name_end == -1:
                return "Type Error in command"
            else:
                return edit(user, "remove", money_start)



    elif kind.find("clear") == 0: #bei clear befehl
        if not kind.find("!") == -1:
            temp = 3
        else:
            temp = 2

        name_start = kind[6:]

        user = name_start[temp:]
        user = user[:-1]

        if not os.path.exists("users/" + str(user) + '.ini'):
            return "Diese Person hat noch keinen Account!"
        else:
            if not name_start.find(" ") == -1:
                return "Type Error in command"
            else:
                return edit(user, "clear")



    elif kind.find("set") == 0:
        if not kind.find("!") == -1:
            temp = 3
        else:
            temp = 2

        name_start = kind[4:]
        name_end = name_start.find(" ")
        name = name_start[:name_end]

        money_start = name_start[name_end + 1:]
        money_end = money_start.find(" ")

        user = name[temp:]
        user = user[:-1]

        if not os.path.exists("users/" + str(user) + '.ini'):
            return "Diese Person hat noch keinen Account!"
        else:
            if name == "" or money_end != -1 or name_end == -1:
                return "Type Error in command"
            else:
                return edit(user, "set", money_start)


    else:
        return "invalid method!"



