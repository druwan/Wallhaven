import requests
import secrets
import random
import time

link_file = open("links.txt", "r")
entries = link_file.readlines()
link_file.close()

number_of_wallpapers = random.randint(10,30)
print(number_of_wallpapers)

i = 0
while i < number_of_wallpapers:
    random_image = random.choice(entries)
    send_to_discord = f"{random_image}"
    data = {"content": send_to_discord, 
            "username": "Wallhaven"
        }
    requests.post(secrets.DiscordWebHook, data=data)
    time.sleep(15)
    i += 1
