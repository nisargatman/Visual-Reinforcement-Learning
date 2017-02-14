import os
from PIL import Image

width = 480
height = 360

os.chdir('SegNet/Images_train') # can change path depending on which images to resize
files = os.listdir(os.getcwd())
n = 0
for file in files:
    img = Image.open(file)
    img = img.resize((width,height),Image.ANTIALIAS)
    img.save('Images/Image%d.jpeg'%n) # depending on path, name is decided
    n = n+1
    if n%100 == 0:
        print n
        
