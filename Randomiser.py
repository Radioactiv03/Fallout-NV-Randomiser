import os, time, random,glob
from shutil import *

direc=input("Please enter your Fallout Data Directory\nEg:C:\Games\GoG\FalloutNewVegas\Data\\\n:")
directory=[r"\\textures\\architecture\\",r"\\textures\\armor\\",r"\\textures\\characters\\",r"\\textures\\clutter\\",r"\\textures\\creatures\\",r"\\textures\\decals\\",r"\\textures\\dungeons\\",r"\\textures\\effects\\",r"\\textures\\fonts\\",r"\\textures\\furniture\\",r"\\textures\\gore\\",r"\\textures\\interface\\barter",r"\\textures\\interface\\companion_wheel",r"\\textures\\interface\\credits",r"\\textures\\interface\\endgame",r"\\textures\\interface\\faders",r"\\textures\\interface\\hotkeys",r"\\textures\\interface\\hud",r"\\textures\\interface\\icons",r"\\textures\\interface\\loading",r"\\textures\\interface\\main",r"\\textures\\interface\\notes",r"\\textures\\interface\\pause",r"\\textures\\interface\\radio wave",r"\\textures\\interface\\shared",r"\\textures\\interface\\stats",r"\\textures\\interface\\target_reticule",r"\\textures\\interface\\vats",r"\\textures\\interface\\worldmap",r"\\textures\\landscape\\",r"\\textures\\pimpboy3billion\\",r"\\textures\\pipboy3000\\",r"\\textures\\projectiles\\",r"\\textures\\shared\\",r"\\textures\\sky\\",r"\\textures\\temp\\",r"\\textures\\terminals\\",r"\\textures\\traps\\",r"\\textures\\trees\\",r"\\textures\\vehicles\\",r"\\textures\\water\\",r"\\textures\\weapons\\"]
audiodirectory=[r"Sound\\fx\\amb",r"Sound\\fx\\drs",r"Sound\\fx\\emt",r"Sound\\fx\\fol",r"Sound\\fx\\fst",r"Sound\\fx\\fx",r"Sound\\fx\\itm",r"Sound\\fx\\mus",r"Sound\\fx\\npc",r"Sound\\fx\\obj",r"Sound\\fx\\phy\\",r"Sound\\fx\\qst",r"Sound\\fx\\temp",r"Sound\\fx\\trp",r"Sound\\fx\\ui",r"Sound\\fx\\voc",r"Sound\\fx\\wpn",r"Sound\\fx\\"]
voicebasedirectory=r"Sound\\Voice\\falloutnv.esm\\"
voicedirectory=[r"creatureferalghoul",r"creaturelowintsm",r"creaturesmartsm",r"creaturesupermutant",r"creatureuniquelily",r"creatureuniquemarcus",r"creatureuniquemrhouse",r"creatureuniquetabitha",r"femaleadult01default",r"femaleadult02",r"femaleadult03",r"femaleadult04",r"femaleadult05",r"femaleadult06",r"femaleadult07",r"femaleadult08",r"femaleadult09",r"femaleadult10",r"femaleadult11",r"femaleadult12",r"femalechild01",r"femalechild02",r"femalegenericghoul",r"femaleghoul02",r"femaleold01",r"femaleold02",r"femaleold03",r"femaleuniquecass",r"femaleuniquemoore",r"femaleuniqueveronica",r"ghouluniqueraul",r"maleadult01default",r"maleadult01defaultb",r"maleadult02",r"maleadult03",r"maleadult04",r"maleadult05",r"maleadult06",r"maleadult07",r"maleadult08",r"maleadult09",r"maleadult10",r"maleadult11",r"maleadult12",r"malechild01",r"malechild02",r"malegenericghoul",r"maleghoul02",r"maleold01",r"maleold02",r"maleuniquearcade",r"maleuniquebenny",r"maleuniquebigsal",r"maleuniquebillyknight",r"maleuniquecaesar",r"maleuniquecolonelhsu",r"maleuniquecraigboone",r"maleuniquedocmitchell",r"maleuniquehanlon",r"maleuniquejasonbright",r"maleuniquelanius",r"maleuniquemrnewvegas",r"maleuniquenarrator",r"maleuniquepapakhan",r"D:/Games/GOGO/FalloutNewVegasRand/Data/Sound/Voice/falloutnv.esm/maleuniquepresident",r"maleuniquetheking",r"maleuniquevulpe",r"playervoicefemale",r"playervoicemale",r"robotede",r"roboteyebot",r"robotfestus",r"robotlibertyprime",r"robotmistergutsy",r"robotmisterhandy",r"robotprotectron",r"robotrobobrain",r"robotsentrybot",r"robotuniquerex",r"robotvictor",r"robotyesman",r"temp"]
temparray=glob.glob(direc+directory[12]+r"\**\*.ddstemp",recursive=True)
SoundRandom=input("Randomise Sounds: True/False\n")
TextureRandom=input("Randomise Textures: True/False\n")
VoiceRandom=input("Random Voices: True/False\n")
print("Randomising")
def randomdds(textdirec):
    array=glob.glob(direc+textdirec+r"/**/*.dds",recursive=True)
    arrayrand=glob.glob(direc+textdirec+r"/**/*.dds",recursive=True)

    random.shuffle(arrayrand)
    x=0
    for texts in array:
        os.rename(texts,arrayrand[x]+"temp")
        x=x+1
    time.sleep(0.1)
    x=random.randint(0,len(arrayrand)-1)
    for text in arrayrand:
        os.rename(text+"temp",array[x])
        x=x-1
        
def randomogg(textdirec):
    array=glob.glob(direc+textdirec+r"/**/*.ogg",recursive=True)
    arrayrand=glob.glob(direc+textdirec+r"/**/*.ogg",recursive=True)
    random.shuffle(arrayrand)
    x=0
    for texts in array:
        os.rename(texts,arrayrand[x]+"temp")
        x=x+1
    time.sleep(0.1)
    x=random.randint(0,len(arrayrand)-1)
    for text in arrayrand:
        os.rename(text+"temp",array[x])
        x=x-1
        
def randomwav(textdirec):
    array=glob.glob(direc+textdirec+r"/**/*.wav",recursive=True)
    arrayrand=glob.glob(direc+textdirec+r"/**/*.wav",recursive=True)
    random.shuffle(arrayrand)
    x=0
    for texts in array:
        os.rename(texts,arrayrand[x]+"temp")
        x=x+1
    time.sleep(0.1)
    x=random.randint(0,len(arrayrand)-1)
    for text in arrayrand:
        os.rename(text+"temp",array[x])
        x=x-1
    
if (TextureRandom.upper()=="TRUE"):
    for textdirec in directory:
        randomdds(textdirec)
else:
    ()
    
if (SoundRandom.upper()=="TRUE"):
    for textdirec in audiodirectory:
        try:
            randomwav(textdirec)
        except ValueError:
            ()
        except IndexError:
            ()
    
    if(VoiceRandom.upper()=="TRUE"):
        for textdirec1 in voicedirectory:
            try:
                textdirec=voicebasedirectory+textdirec1
                randomogg(textdirec)
            except ValueError:
                ()
            except IndexError:
                ()
        else:
            ()
print("done")
input("Press Enter To Close")
