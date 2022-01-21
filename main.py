from PIL import Image
import json
import random
import threading
from itertools import repeat
from getLayersWithDetails import buildLayersDict
from utils import fillFilenameArray
import os

"""
Watch out on the syntax and make sure to add a new trait all over the script if you add one. Same goes for removing a trait.
"""
layers = buildLayersDict()
print(layers)

whole = [] # for duplicate check

"""
Creates random shuffled lists of each trait category with all its traits and their desired quantity.
"""
ojosList = []
for x in layers['ojos']:
    ojosList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(ojosList)

orejasAList = []
for x in layers['orejasA']:
    orejasAList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(orejasAList)

orejasBList = []
for x in layers['orejasB']:
    orejasBList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(orejasBList)

orejasCList = []
for x in layers['orejasC']:
    orejasCList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(orejasCList)

cuerpoList = []
for x in layers['cuerpo']:
    cuerpoList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(cuerpoList)

narizList = []
for x in layers['nariz']:
    narizList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(narizList)

poloList = []
for x in layers['polo']:
    poloList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(poloList)

aretesList = []
for x in layers['aretes']:
    aretesList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(aretesList)

fondosList = []
for x in layers['fondos']:
    fondosList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(fondosList)

herramientaList = []
for x in layers['herramienta']:
    herramientaList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(herramientaList)

brazosList = []
for x in layers['brazos']:
    brazosList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(brazosList)

cuernosList = []
for x in layers['cuernos']:
    cuernosList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(cuernosList)

bocaList = []
for x in layers['boca']:
    bocaList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(bocaList)

gorraList = []
for x in layers['gorra']:
    gorraList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(gorraList)

frenteList = []
for x in layers['frente']:
    frenteList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(frenteList)

rayoList = []
for x in layers['rayo']:
    rayoList.extend(repeat(x['Trait'], int(x['Quantity'])))
random.shuffle(rayoList)

path = 'images/' # standard path to the images directory

"""
Please keep the same format which is having Eyes_ for example at least before the actual trait name. Don't forget .png or .jpg or whatever at the end.
"""
ojos = fillFilenameArray('ojos')
ojo = ''
orejasA = fillFilenameArray('orejasA')
orejaA = ''
orejasB = fillFilenameArray('orejasB')
orejaB = ''
orejasC = fillFilenameArray('orejasC')
orejaC = ''
cuerpos = fillFilenameArray('cuerpo')
cuerpo = ''
narizs = fillFilenameArray('nariz')
nariz = ''
polos = fillFilenameArray('polo')
polo = ''
aretes = fillFilenameArray('aretes')
arete = ''
fondos = fillFilenameArray('fondos')
fondo = ''
herramientas = fillFilenameArray('herramienta')
herramienta = ''
brazos = fillFilenameArray('brazos')
brazo = ''
cuernos = fillFilenameArray('cuernos')
cuerno = ''
bocas = fillFilenameArray('boca')
boca = ''
gorras = fillFilenameArray('gorra')
gorra = ''
frentes = fillFilenameArray('frente')
frente = ''
rayos = fillFilenameArray('rayo')
rayo = ''

def gen():
    count = 0
    while count != 17: # size of collection, so script stops
        traits = []

        traits_names = []

        """
        Collecting of the randomly chosen traits.
        """
        ojosCheck = random.choice(ojosList)
        ojosList.remove(ojosCheck)
        for x in ojos:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == ojosCheck:
                ojo = x
                print(x)
                break
        
        orejasACheck = random.choice(orejasAList)
        orejasAList.remove(orejasACheck)
        for x in orejasA:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == orejasACheck:
                orejaA = x
                print(x)
                break

        orejasBCheck = random.choice(orejasBList)
        orejasBList.remove(orejasBCheck)
        for x in orejasB:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == orejasBCheck:
                orejaB = x
                print(x)
                break
        
        orejasCCheck = random.choice(orejasCList)
        orejasCList.remove(orejasCCheck)
        for x in orejasC:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == orejasCCheck:
                orejaC = x
                print(x)
                break
        
        cuerposCheck = random.choice(cuerpoList)
        cuerpoList.remove(cuerposCheck)
        for x in cuerpos:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == cuerposCheck:
                cuerpo = x
                print(x)
                break
        
        narizCheck = random.choice(narizList)
        narizList.remove(narizCheck)
        for x in narizs:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == narizCheck:
                nariz = x
                print(x)
                break    

        polosCheck = random.choice(poloList)
        poloList.remove(polosCheck)
        for x in polos:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == polosCheck:
                polo = x
                print(x)
                break    

        aretesCheck = random.choice(aretesList)
        aretesList.remove(aretesCheck)
        for x in aretes:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == aretesCheck:
                arete = x
                print(x)
                break    
        
        fondosCheck = random.choice(fondosList)
        fondosList.remove(fondosCheck)
        for x in fondos:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == fondosCheck:
                fondo = x
                print(x)
                break
        
        herramientasCheck = random.choice(herramientaList)
        herramientaList.remove(herramientasCheck)
        for x in herramientas:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == herramientasCheck:
                herramienta = x
                print(x)
                break  

        brazosCheck = random.choice(brazosList)
        brazosList.remove(brazosCheck)
        for x in brazos:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == brazosCheck:
                brazo = x
                print(x)
                break  

        cuernosCheck = random.choice(cuernosList)
        cuernosList.remove(cuernosCheck)
        for x in cuernos:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == cuernosCheck:
                cuerno = x
                print(x)
                break

        bocasCheck = random.choice(bocaList)
        bocaList.remove(bocasCheck)
        for x in bocas:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == bocasCheck:
                boca = x
                print(x)
                break   

        gorrasCheck = random.choice(gorraList)
        gorraList.remove(gorrasCheck)
        for x in gorras:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == gorrasCheck:
                gorra = x
                print(x)
                break 

        frentesCheck = random.choice(frenteList)
        frenteList.remove(frentesCheck)
        for x in frentes:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == frentesCheck:
                frente = x
                print(x)
                break

        rayosCheck = random.choice(rayoList)
        rayoList.remove(rayosCheck)
        for x in rayos:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == rayosCheck:
                rayo = x
                print(x)
                break
            
        traits.extend((fondo, cuerpo, brazo, polo, herramienta, orejaA,orejaB, orejaC, frente, cuerno, ojo, nariz, arete, boca, gorra, rayo)) # putting all traits for this NFT in a list (make sure to choose your order of layering by this list from left to right)
        print(traits)
        print(count)
        for trait in traits:
            trait = trait.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] # getting the exact trait names from the file name
            traits_names.append(trait)
            
        if traits not in whole: # duplicate check

            whole.append(traits)

            for trait in traits:
                if 'fondos' in trait:
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
            fondosList.append(traits_names[0])
            cuerpoList.append(traits_names[1])
            brazosList.append(traits_names[2])
            poloList.append(traits_names[3])
            herramientaList.append(traits_names[4])
            orejasAList.append(traits_names[5])
            orejasBList.append(traits_names[6])
            orejasCList.append(traits_names[7])
            frenteList.append(traits_names[8])
            cuernosList.append(traits_names[9])
            ojosList.append(traits_names[10])
            narizList.append(traits_names[11])
            aretesList.append(traits_names[12])
            bocaList.append(traits_names[13])
            gorraList.append(traits_names[14])
            rayoList.append(traits_names[15])
    else:
        print('Successfully Generated All NFTs!')

threading.Thread(target=gen(), args=()).start() # thread to start the gen, feel free to add more function and threads to speed up the generation process
