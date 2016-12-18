from PIL import Image
import os

def distance(x,y):
    dist = ((x[0]-y[0])**2)+((x[1]-y[1])**2)+((x[2]-y[2])**2)
    return dist

def work():
    os.chdir('SegNet/Images_label')
    files = os.listdir(os.getcwd())

    wall = (0,0,0)
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
    bed = [(89,41,93),(41,133,68)]

    n = 0
    for file in files:
        image = Image.open(file)
        pixels = list(image.getdata())
        label = [None]*(460*680)
        min_dist = 10000000 # large random number
        for i in range(480*640):
            pix = pixels[i]
            dist = distance(pix,wall)
            if dist<min_dist:
                label[i] = 0
                min_dist = dist
            dist = distance(pix,floor[0])
            if dist<min_dist:
                label[i] = 1
                min_dist = dist
            dist = distance(pix,floor[1])
            if dist<min_dist:
                label[i] = 1
                min_dist = dist
            dist = distance(pix,glass[0])
            if dist<min_dist:
                label[i] = 2
                min_dist = dist
            dist = distance(pix,glass[1])
            if dist<min_dist:
                label[i] = 2
                min_dist = dist
            dist = distance(pix,carpet[0])
            if dist<min_dist:
                label[i] = 3
                min_dist = dist
            dist = distance(pix,carpet[1])
            if dist<min_dist:
                label[i] = 3
                min_dist = dist
            dist = distance(pix,bookcase[0])
            if dist<min_dist:
                label[i] = 4
                min_dist = dist
            dist = distance(pix,bookcase[1])
            if dist<min_dist:
                label[i] = 4
                min_dist = dist
            dist = distance(pix,bed[0])
            if dist<min_dist:
                label[i] = 5
                min_dist = dist
            dist = distance(pix,bed[1])
            if dist<min_dist:
                label[i] = 5
                min_dist = dist
            dist = distance(pix,cupboard)
            if dist<min_dist:
                label[i] = 6
                min_dist = dist
            dist = distance(pix,door)
            if dist<min_dist:
                label[i] = 7
                min_dist = dist
            dist = distance(pix,computer)
            if dist<min_dist:
                label[i] = 8
                min_dist = dist
            dist = distance(pix,fireplace)
            if dist<min_dist:
                label[i] = 9
                min_dist = dist
            for j in range(len(furniture)):
                dist = distance(pix,furniture[j])
                if dist<min_dist:
                    label[i] = 10
                    break
        n = n+1
        print n

if __name__ == "__main__":
    print distance((0,0,0),(1,1,1))