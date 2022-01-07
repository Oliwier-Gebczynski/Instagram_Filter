import instaloader
from Instagram_Profiler.login import *

def get_names():
    connection = instaloader.Instaloader()
    connection.login(login, password)

    name_acc = input("Account name: ")

    profile = instaloader.Profile.from_username(connection.context, name_acc)

    follow_list = []

    for item in profile.get_followees():
        follow_list.append(item.username)

    return follow_list

def filtr_acc():
    #filtrowanie osób, tylko ponad 1000 follow zeby odfiltrować znajomych ( duża część znajomych ma poniżej 1k follow )


