import os
import functions

def delu(user):
    user = str(user)
    if not user.find("!") == -1:
        temp = 3
    else:
        temp = 2

    user = user[temp:]
    user = user[:-1]

    if not os.path.exists("users/" + str(user) + '.ini'):
        return "Diese Person hat noch keinen Account!"
    else:
        name = functions.name(user)
        os.remove("users/" + str(user) + '.ini')
        return "User " + name + " deleted"
