#! /usr/bin/env python3
import json
import os
import requests
import glob
# This example shows how a file can be uploaded using
# The Python Requests module

fruits_data = {}
images = glob.glob("*/*/*.jpeg", recursive=True)
def JSONupload(path, images):
    with open(path, 'rb') as file:
            lines = file.read().decode().split("\n")
            name = lines[0].strip()
            weight = int(lines[1].split(" ")[0])
            description = lines[2].strip()
            image_name = lines[3].strip()
            print(image_name)
            for image in images:
                entry = {
                "name" : name,
                "weight": weight,
                "description": description,
                "image_name": image
                }
                fruits_data = entry
                headers = {"Content-Type": "application/json"}
                url = "http://localhost/fruits/"
                r = requests.post(url, data=json.dumps(fruits_data), headers=headers)
                if r.status_code == 200:
                    print("Data posted successfully!")
                else:
                    print("Failed to post data. Status code:", r.status_code)
paths = glob.glob("*/descriptions/*.txt", recursive=True)
for path in paths:
    JSONupload(path, images)


