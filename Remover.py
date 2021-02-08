import os,glob
suffix = "_n.dds"
path=os.getcwd()
lod=r"Textures\Landscape\Lod\\"
pipboy=r"Textures\\pipboy3000"
annoydir=[r"Sound\\fx\\amb\\amb_desertdefault\\"]
directory=[lod]
print("Deleting normal files")
for name in glob.glob(path+"/**/*.dds", recursive=True): 
    if(name.endswith("_n.dds")==True):
        os.remove(name)
    elif(name.endswith("screenglare.dds")==True):
        os.remove(name)
def fileremover(text):    
    for name in (glob.glob(path+text+r"/**/*.dds",recursive=True)):
        try:
            os.remove(name)
        except FileNotFoundError:
            ()
    for name in (glob.glob(path+text+r"/**/*.ddstemp",recursive=True)):
        try:
            os.remove(name)
        except FileNotFoundError:
            ()
    for name in (glob.glob(path+pipboy+r"/*.dds")):
        os.remove(name)
def fileremoversound(text):
    for name in (glob.glob(path+text+r"/**/*.wav",recursive=True)):
        os.remove(name)
        
for text in directory:
    fileremover(text)
for text in annoydir:
    fileremoversound(text)
print("done!")
input("Press Enter To Close")
