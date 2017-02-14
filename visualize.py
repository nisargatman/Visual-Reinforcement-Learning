import sys
import numpy as np
from PIL import Image

points = [(0,0,0),(83,101,27),(94,113,31),(160,112,138),(151,10,115),(230,218,232),(127,124,135),(23,122,55),(146,96,69),(110,72,53),(172,20,27),(110,89,84),(106,85,82),
        (150,37,0),(204,199,11),(198,63,36),(143,100,58),(129,84,53),(158,103,72),(139,90,58),(144,135,104),(233,222,190),(120,172,185),(180,89,32),(89,41,93),(41,133,68)]
labels = {1:[0],2:[1,2],3:[3,4],4:[5,6],5:[7],6:[8,9],7:[10],8:[11,12,13,14,15,16,17,18,19,20,21],9:[22],10:[23],11:[24,25]}

def visualize(image):
    width, height = image.size
    data = np.zeros( (height,width,3), dtype=np.uint8)
    pixels = list(image.getdata())
    for i, pixel in list(enumerate(pixels)):
        r = i/width
        c = i%width
        code = pixel[0] + 1
        try:
            val = labels[code]
        except:
            val = [1]
        point = points[val[0]]
        data[r,c] = point
    im = Image.fromarray(data)
    im.show()

if __name__ == '__main__':
    image = Image.open(sys.argv[1])
    visualize(image)