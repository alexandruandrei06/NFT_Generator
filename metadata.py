import pandas as pd
import numpy as np
import random
import time
import os
from progressbar import progressbar
import json
from copy import deepcopy


# Base metadata. MUST BE EDITED.
BASE_IMAGE_URL = "ipfs://bafybeicpugja5v5spdc27cwzhqxuu3nyfnttrqohrb4hczvw4z5cepadmu"
BASE_NAME = "MultiCourseX Teacher"

BASE_JSON = {
    "name": BASE_NAME,
    "description": "MultiCourseX Teacher NFT",
    "image": BASE_IMAGE_URL,
    "attributes": [],
}

def generate_metadata(metadata_path, edition_name):
    numberOfNFTs = len(os.listdir(os.path.join('output', edition_name)))
    for i in range(0, numberOfNFTs + 1):
        item_json = deepcopy(BASE_JSON)

        item_json['name'] = BASE_NAME + " #" + str(i)
        
         # Append image PNG file name to base image path
        item_json['image'] = item_json['image'] + '/' + str(i) + '.png'
        # Adding attributes
        item_json['attributes'].append({ 'trait_type': 'Teacher Index', 'value': i })

        with open(os.path.join(metadata_path, str(i) + '.json'), 'w') as f:
            json.dump(item_json, f)

def main():
   # Get edition name
    edition_name = ""
    edition_path = ""

    while True:
        edition_name = input("Enter edition you want to generate metadata for: ")
        if edition_name == "":
            print("Oops! Looks like this edition doesn't exist! Check your output folder to see what editions exist.")
            continue
        edition_path = os.path.join('output', edition_name)
        if os.path.exists(edition_path):
                print("Edition exists! Generating JSON metadata...")
                break
        else:
            print("Oops! Looks like this edition doesn't exist! Check your output folder to see what editions exist.")
    
    if not os.path.exists('metadata'):
        os.makedirs('metadata')
    
    if not os.path.exists(os.path.join('metadata', edition_name)):
        os.makedirs(os.path.join('metadata', edition_name))

    metadata_path = os.path.join('metadata', edition_name)

    generate_metadata(metadata_path, edition_name)

main()