# NFT_Generator

Python scripts that generates NFTs images and metadata for a NFT collection.

# Upload IPFS

After generating the images, enter on https://nft.storage/ , add the folder using NFTUp, and get the CID.

After getting the CID, go to metadata.py, and add CID to BASE_IMAGE_URL. Modify BASE_JSON as you need.

Upload the metadata on https://car.ipfs.io and download .car file. Upload that on https://nft.storage/ and get the CID.

BaseURI for NFT collection: https://ipfs.io/ipfs/{CID}/

# Usage

For generating the images of the collection:

```bash
python3 nft.py
```

```python
Enter the amount of NFTs to generate: {amount}
Enter the base for the NFTs: {pathToBase}
Enter the output folder for NFTs: {outputFile}
```

For generating the metadate of the collection:

```bash
python3 metadata.py
```

```python
Enter edition you want to generate metadata for: {NFT_Collection}
Edition exists! Generating JSON metadata...
```

{NFT_Collection} must be the name of the folder from the /output with the NFTs.

# Totorial

This is a tutorial for generating NFT colection with rarity traits and random/weighted traits

https://dev.to/balt1794/how-to-create-nft-pixel-art-much-exclusive-doge-yacht-club-collection-part-iii-python-library-2cp4

https://www.youtube.com/watch?v=LUDEkicL2Gs&list=PLa0hmV2hTFg4UJnDk-30ZEXU4VPwtZL2H&index=1
