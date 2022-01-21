from PIL import Image
import json
import random
import threading
from itertools import repeat
from getLayersWithDetails import buildLayersDict
import os

I = 3

"""
Watch out on the syntax and make sure to add a new trait all over the script if you add one. Same goes for removing a trait.
"""
layers = buildLayersDict()

whole = [] # for duplicate check

"""
Creates random shuffled lists of each trait category with all its traits and their desired quantity.
"""
backgroundsList = []
for x in layers['Backgrounds']:
    backgroundsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(backgroundsList)
skinsList = []
for x in layers['Skins']:
    skinsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(skinsList)
mouthsList = []
for x in layers['Mouths']:
    mouthsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(mouthsList)
eyesList = []
for x in layers['Eyes']:
    eyesList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(eyesList)
overheadsList = []
for x in layers['Over Heads']:
    overheadsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(overheadsList)

path = 'images/' # standard path to the images directory

"""
Please keep the same format which is having Eyes_ for example at least before the actual trait name. Don't forget .png or .jpg or whatever at the end.
"""
bgs = ['01_BG_BlueSpace.png', '02_BG_PurpleBokeh.png', '03_BG_StringLigth.png', '04_BG_Space.png', '05_BG_Moon.png', '06_BG_Hallowen.png', '07_BG_SkyDreams.png', '08_BG_Grey.png', '09_BG_HardGrey.png', '10_BG_EnergySolana.png', '11_BG_Blue.png', '12_BG_BlueDiamond.png', '13_BG_SkyBlue.png', '14_BG_CloudSky.png', '15_BG_Pink.png', '16_BG_ChicSquare.png', '17_BG_NegativeLight.png', '18_BG_Sunset.png', '19_BG_True Mist.png', '20_BG_Aurora borealis.png']
bg = ''
skins = ['01_Skins_Base.png', '02_Skins_DarkBlocks.png', '03_Skins_VioletFlower.png', '04_Skins_Emerald.png', '05_Skins_Rubi.png', '06_Skins_Stone.png', '07_Skins_Gold.png', '08_Skins_Glacial.png', '09_Skins_PinkCuarzo.png', '10_Skins_PurpleGemmorado.png', '11_Skins_OLava.png', '12_Skins_GrungePink.png', '13_Skins_Rainbow.png', '14_Skins_Zombie.png', '15_Skins_BlueJelly.png', '16_Skins_RedJelly.png', '17_Skins_SmothEnergy.png', '18_Skins_PowerEnergy.png', '19_Skins_Wood.png', '20_Skins_DarkEnergy.png']
skin = ''
mouths = ['01_Mouth_Zombie.png', '02_Mouth_Vampiro.png', '03_Mouth_Dienton.png', '04_Mouth_Monsta.png', '05_Mouth_Rude.png', '06_Mouth_Vampire2.png', '07_Mouth_Sunrise.png', '08_Mouth_Tiburoncin.png', '09_Mouth_Lenguita.png', '10_Mouth_Sonrisa.png', '11_Mouth_Smile.png', '12_Mouth_Macabro.png', '13_Mouth_Thuglife.png']
mouth = ''
eyez = ['01_Eyes_Vampiro.png', '02_Eyes_Suspicaz.png', '03_Eyes_Enojado.png', '04_Eyes_Evil.png', '05_Eyes_Boton.png', '06_Eyes_Reptilian.png', '07_Eyes_Frog.png', '08_Eyes_Jelly.png', '09_Eyes_Machine.png', '10_Eyes_Visor.png', '11_Eyes_Mee.png', '12_Eyes_Kawai.png', '13_Eyes_Enforced.png', '14_Eyes_Wheel.png', '15_Eyes_Woman.png', '16_Eyes_OneEye.png', '17_Eyes_Sadness.png', '18_Eyes_Thuglife.png']
eyes = ''
overheads = ['01_Overhead_Astronaut.png', '02_Overhead_HermesWings.png', '03_Overhead_Crown.png', '04_Overhead_RedHat.png', '05_Overhead_Christmas hat.png']
overhead = ''

def gen():
    count = 0
    while count != 10: # size of collection, so script stops
        traits = []

        traits_names = []

        """
        Collecting of the randomly chosen traits.
        """
        bgcheck = random.choice(backgroundsList)
        backgroundsList.remove(bgcheck)
        print(bgs)
        for x in bgs:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == bgcheck:
                bg = x
                print(x)
                break

        skincheck = random.choice(skinsList)
        skinsList.remove(skincheck)
        for x in skins:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == skincheck:
                skin = x
                break

        mouthcheck = random.choice(mouthsList)
        mouthsList.remove(mouthcheck)
        for x in mouths:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == mouthcheck:
                mouth = x
                break

        eyescheck = random.choice(eyesList)
        eyesList.remove(eyescheck)
        for x in eyez:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == eyescheck:
                eyes = x
                break

        overheadcheck = random.choice(overheadsList)
        overheadsList.remove(overheadcheck)
        for x in overheads:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == overheadcheck:
                overhead = x
                print(overhead)
                break

        traits.extend((bg, skin, mouth, eyes, overhead)) # putting all traits for this NFT in a list (make sure to choose your order of layering by this list from left to right)
        print(traits)
        print(count)
        for trait in traits:
            trait = trait.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] # getting the exact trait names from the file name
            traits_names.append(trait)
            
        if traits not in whole: # duplicate check

            whole.append(traits)

            for trait in traits:
                if 'BG' in trait:
                    nft = Image.open(path+trait).convert('RGBA') # important for background
                else:
                    trait = Image.open(path+trait)
                    nft = Image.alpha_composite(nft, trait) # layer process of each trait
            
            """
            This is the most dangerous part. Please triple check your metadata because 95% of all errors when uploading to a Candy Machine are caused by wrong metadata.
            Please remove the comments from it if you are done with setup xd.
            """
            metadata = {
                "name":f"Sellos #{count+1}","symbol":"", # +1 because metadata files need to start with 0 but your NFT obviously has the number 1
                "description":"This is my awesome collection of Nfts.", # description of your project
                "seller_fee_basis_points":500,"image":f"{count}.png","external_url":"https://blacyagencia.com/", # 500 stands for 5% royalties on marketplaces and external_url is your project's website
                "attributes":[
                    {"trait_type":"Background","value":traits_names[0]}, # number in the brackets is the index number of the trait in the list where you decided the layer order
                    {"trait_type":"Skin","value":traits_names[1]},
                    {"trait_type":"Mouth","value":traits_names[2]},
                    {"trait_type":"Eyes","value":traits_names[3]},
                    {"trait_type":"Over Head","value":traits_names[4]}],
                    "collection":{"name":"Project","family":"Project"},
                    "properties":{"files":[{"uri":f"{count}.png","type":"image/png"}],
                    "category":"image","maxSupply":1,"creators":[{"address":"BUkGkSTEtusFLpmZHwC9jzVUqpDKDL83dWzTrr8vAZqc","share":100}]} # 100 means 100% of the royalties' proceeds and you can add more to split it
            }

            nft.save(f'results/{count}.png',"PNG") # saving of the generated NFT

            metadata = json.dumps(metadata)
            metadataFile = open(f"results/{count}.json", "w")
            metadataFile.write(metadata) # saving of the metadata of this generated NFT
            metadataFile.close()

            count += 1

        else: # add traits to the list when a duplicate is found
            backgroundsList.append(traits_names[0])
            skinsList.append(traits_names[1])
            mouthsList.append(traits_names[2])
            eyesList.append(traits_names[3])
            overheadsList.append(traits_names[4])


    else:
        print('Successfully Generated All NFTs!')

threading.Thread(target=gen(), args=()).start() # thread to start the gen, feel free to add more function and threads to speed up the generation process
