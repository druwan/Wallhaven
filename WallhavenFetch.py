import requests
import secrets
import time
import random

def fetchWallpapers(url, first_response, number_of_pages):
    for page in range(1, last_page):
        # print(page)
        time.sleep(1)
        if page % 45 == 0:
            print("Waiting for next call request")
            time.sleep(20)
        base_data = requests.get(base_URL + f"&page={page}").json()    
        i = 0
        while i < 24:
            path_array.append(base_data["data"][i].get("path"))
            i += 1
    return path_array


def toDiscord(path_array, number_of_images):
    # Select a random picture to send to discord
    i = 1
    while i <= number_of_images:
        random_image = random.choice(path_array)
        send_to_discord = f"URL: \n {random_image}"
        data = {"content": send_to_discord, "username": "Wallhaven"}
        requests.post(secrets.DiscordWebHook,data=data)
        print(f"Sent: {random_image}")
        i += 1


def savetext(path_array):
    # Save a txt of all wallpapers
    link_file = open("links.txt", "w")
    for link in path_array:
        link_file.write(link + "\n")
    link_file.close()


# Main Program
base_URL = f"https://wallhaven.cc/api/v1/collections/{secrets.USERNAME}/{secrets.folder_id}?apikey={secrets.api_key}"
base_data = requests.get(base_URL).json()
last_page = base_data["meta"].get("last_page")
path_array = []

fetchWallpapers(base_URL, base_data, last_page)
copy_of_array = path_array[:]
toDiscord(copy_of_array, 20)
savetext(copy_of_array)