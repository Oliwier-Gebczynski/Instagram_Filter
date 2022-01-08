import instaloader
from IF.login import *
from bs4 import BeautifulSoup
import requests

def get_names():
    connection = instaloader.Instaloader()
    connection.login(login, password)

    name_acc = input("Account name: ")
    profile = instaloader.Profile.from_username(connection.context, name_acc)
    follow_list = []

    for item in profile.get_followees():
        if filtr_acc(item.username) > 1000:
            follow_list.append(item.username)

    return follow_list

def filtr_acc(name):
    url = f"https://www.instagram.com/{name}/"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    meta = doc.find("meta", property="og:description")
    result_list = meta.attrs['content'].split(" ")

    result = result_list[-1]
    return result


get_names()

# projekt przerwany do momenty odblokowania konta
