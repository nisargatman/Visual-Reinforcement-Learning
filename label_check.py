from PIL import Image
import os
import numpy as np

'''wall = (0,0,0)
    floor = [(83,101,27),(94,113,31)]
    glass = [(160,112,138),(151,10,115)]
    carpet = [(230,218,232),(127,124,135)]
    computer = (23,122,55)
    bookcase = [(146,96,69),(110,72,53)]
    fireplace = (172,20,27)
    #flower = [(193,95,94),(121,104,60)]
    furniture = [(110,89,84),(106,85,82),(150,37,0),(204,199,11),(198,63,36),(143,100,58),(129,84,53),(158,103,72),(139,90,58),(144,135,104),(233,222,190)]
    cupboard = (120,172,185)
    door = (180,89,32)
    bed = [(89,41,93),(41,133,68)]'''

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


points = [(0,0,0),(83,101,27),(94,113,31),(160,112,138),(151,10,115),(230,218,232),(127,124,135),(23,122,55),(146,96,69),(110,72,53),(172,20,27),(110,89,84),(106,85,82),
        (150,37,0),(204,199,11),(198,63,36),(143,100,58),(129,84,53),(158,103,72),(139,90,58),(144,135,104),(233,222,190),(120,172,185),(180,89,32),(89,41,93),(41,133,68)]
labels = {1:[0],2:[1,2],3:[3,4],4:[5,6],5:[7],6:[8,9],7:[10],8:[11,12,13,14,15,16,17,18,19,20,21],9:[22],10:[23],11:[24,25]}

def distance(x,y):
    dist = ((x[0]-y[0])**2)+((x[1]-y[1])**2)+((x[2]-y[2])**2)
    return dist

def work():
    os.chdir('SegNet/Images_label/TextureMaps')
    files = os.listdir(os.getcwd())

    for n in xrange(len(files)):
        image = Image.open('TextureMap%d.jpeg'%n)
        width,height = image.size
        label = np.zeros((height,width))
        lab = 0
        pixels = list(image.getdata())
        for i,pixel in list(enumerate(pixels)):
            #print 'Start pixel'
            r = i/width
            c = i%width
            mindist = distance(pixel,points[0])
            #print mindist
            ind = 0
            for index,point in list(enumerate(points)):
                dist = distance(point,pixel)
                #print 'Test a known colour %d distance is:'%index
                #print dist
                if dist < mindist:
                    #print 'Looks like a good distance'
                    ind = index
                    mindist = dist
            for key,value in labels.iteritems():
                if ind in value:
                    label[r,c] = key
        label = Image.fromarray(label)
        label = label.convert('RGB')
        label.save('../Labels/Label%d.jpeg'%n)
        print n
            

if __name__ == "__main__":
    #os.chdir('SegNet/Images_label/Labels')
    #image = Image.open('Label1.jpeg')
    #visualize(image)
    work()
    '''os.chdir('SegNet/Images_label/TextureMaps')
    files = os.listdir(os.getcwd())
    for file in files:
        image = Image.open(file)
        pixels = list(image.getdata()) # print len(pixels) --> 307200; print len(pixels[1]) --> 3; print type(pixels[1]) --> tuple'''
        