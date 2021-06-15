import requests
import secrets
import time
import random

def fetchWallpapers(url, first_response, number_of_pages):
    for page in range(1, last_page):
        print(page)
        time.sleep(1.5)
        if page % 44 == 0:
            print("Waiting for next call request")
            time.sleep(20)
        base_data = requests.get(base_URL + f"&page={page}").json()    
        i = 0
        while i < 24:
            path_array.append(base_data["data"][i].get("path"))
            i += 1
    return path_array

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
savetext(copy_of_array)