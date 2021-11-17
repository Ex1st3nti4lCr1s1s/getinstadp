import requests
import os
import json
import shutil
import json

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
}


# fp = open("names.txt", "r") Uncomment to download from a list. 
fp = input("Enter the username: ")
for cnt, line in enumerate(fp):
    new = str(line.strip())
    url = "https://www.instagram.com/"+new+"/?__a=1"
    print(url)
    link = str(url)

    response = requests.get(link, headers=header).json()

    hd_image_location = response["graphql"]["user"]["profile_pic_url_hd"]

    hd_image_response = requests.get(hd_image_location, stream=True)
    with open(f"{new}.jpg", "wb") as out_file:
        shutil.copyfileobj(hd_image_response.raw, out_file)
