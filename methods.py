from color_rgb import colors
from PIL import Image
import os
import shutil

#cutting display name if needed
def getDisplayName(foldername):
    if len(foldername)>50:
        displayname = foldername[-50:]
        cut = displayname.find("/")
        displayname = "[...]" + displayname[cut:]
    else:
        displayname = foldername 
    return displayname

#getting dominant color of the image
def getDomColor(filepath):
    org_img = Image.open(filepath)
    img = org_img.copy()
    img.convert("RGB")
    img.resize((1, 1), resample=0)
    domcolor = img.getpixel((0, 0))
    return domcolor

#comparing rgb to determine name of the color
def compareColor(image_color):
    manhattan = lambda x,y : abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2]) 
    distances = {k: manhattan(v, image_color) for k, v in colors.items()}
    color = min(distances, key=distances.get)
    return color
    
#moving image to new folder
def moveImage(folderpath, color, filename):
    newfolder = folderpath+"/"+color
    if os.path.isdir(newfolder)==False:
        os.mkdir(newfolder)
    filepath = folderpath+"/"+filename
    newpath = folderpath+"/"+color+"/"+filename
    shutil.move(filepath, newpath)