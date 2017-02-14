import random

c = []
with open('train.txt','a') as f:
    for i in xrange(10000):
        ctr = random.randint(0,10852)
        f.write("/home/nisarg/Visual-Reinforcement-Learning/SegNet/Images_train/Images/Image%s.jpeg"%ctr)
        f.write(" ")
        f.write("/home/nisarg/Visual-Reinforcement-Learning/SegNet/Images_label/Labels/Label%s.jpeg"%ctr)
        c.append(ctr)

original = set(c)
full = set(xrange(min(original), max(original)+1))
missing = sorted(full - original)

with open('test.txt', 'a') as f:
    for i in missing:
        f.write("/home/nisarg/Visual-Reinforcement-Learning/SegNet/Images_train/Images/Image%s.jpeg"%i)
        f.write(" ")
        f.write("/home/nisarg/Visual-Reinforcement-Learning/SegNet/Images_label/Labels/Label%s.jpeg"%i)