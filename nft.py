# Import required libraries
from PIL import Image
import pandas as pd
import numpy as np
import time
import os
import random
from progressbar import progressbar


# Generate a single image given an array of filepaths representing layers
def generate_single_image(filepaths, outputFileName, outputDirName):

    # Treat the first layer as the background
    bg = Image.open(os.path.join('assets', filepaths[0])).convert("RGBA")
    
    
    # Loop through layers 1 to n and stack them on top of another
    for filepath in filepaths[1:]:
        if filepath.endswith('.png'):
            img = Image.open(os.path.join('assets', filepath)).convert("RGBA")
            bg.paste(img, (0,0), img)

    if not os.path.exists('output'):
            os.makedirs('output')
    
    if not os.path.exists(os.path.join('output', outputDirName)):
            os.makedirs(os.path.join('output', outputDirName))
    
    # Save the final image into desired location
    bg.save(outputFileName)
   

def generate_filepaths(BasePath, numberOfNFTs):
    filePaths = []
    for index in range(0, numberOfNFTs + 1):
        filePath = []
        filePath.append(BasePath)
        for i in range(1, 6):
            filePath.append("Number" + str(i) + "/" + str((index // pow(10, i - 1)) % 10) + ".png")
        filePaths.append(filePath)
    return filePaths

def generate_NFTs(filePaths, numberOfNFTs, outputDirName):
    for i in range(0, numberOfNFTs):
        generate_single_image(filePaths[i], "output/" + outputDirName + "/" + str(i) + ".png", outputDirName)

def main():
    numberOfNFTs = int(input("Enter the amount of NFTs to generate: "))
    BasePath = input("Enter the base for the NFTs: ")
    outputDirName = input("Enter the output folder for NFTs: ")

    # Generate filepaths of the elements for every NFT
    filePaths = generate_filepaths(BasePath, numberOfNFTs)

    # Generate images from the filePaths of the elements for every NFT
    generate_NFTs(filePaths, numberOfNFTs, outputDirName)
    

main()