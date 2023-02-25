from PIL import Image
import random

# canvasSize 
w = 29
h = 39
backgroundColor = random.choice(['#f72585','#7209b7', '#4cc9f0'])

# build background
im = Image.new('RGBA', (w, h), backgroundColor)

# add background details
borderColor = random.choice([(255, 214, 255), (187, 208, 255)])

def border():
    for i in range(w):
        if i % 2 == 0:
            im.putpixel((i,0),borderColor)
            im.putpixel((i,h-1),borderColor)

    for i in range(h):
        if i % 2 == 0:
            im.putpixel((0,i),borderColor)
            im.putpixel((w-1,i),borderColor)

def sprinkles():
    for i in range(10):
        x = random.randint(0, 28)
        y = random.randint(0, 38)
        im.putpixel((x,y), borderColor)

# add flower stem
stemColor = (49, 168, 40)
stemShade = (12, 77, 8)

# stem ribbon
ribbonColor = (185, 0, 191)
ribbonShade = (127, 30, 130)

ribbonColors = [(9,29),(9,28),(10,29),(10,28),(11,29),(11,28),(12,29),(12,28)]
ribbonShades = [(11,28),(12,29),(12,28)]

for point in ribbonColors:
    im.putpixel(point, ribbonColor)

for point in ribbonShades:
    im.putpixel(point, ribbonShade)

# stem style 1
# green stem
greenPoints = [(8,30),(8,31),(8,32),(9,19),(9,20),(9,30),(9,31),(9,32),(10,19),(10,20),(10,21),(10,22),(10,23),(10,24),(10,25),(10,26),(10,27),(10,30),(10,31),(10,32),(11,19),(11,20),(11,21),(11,22),(11,23),(11,24),(11,25),(11,26),(11,27),(11,30),(11,31),(11,32),(12,20),(12,21),(12,22),(12,23),(12,24),(12,25),(12,26),(12,27),(13,20),(13,21),(13,22),(13,23),(13,24),(13,25),(13,26),(14,20),(14,21),(14,22),(14,23),(14,24),(14,25),(15,20),(15,21),(15,22),(15,23),(15,24),(16,20),(16,21),(16,22),(16,23),(17,20),(17,21),(17,22),(18,20),(18,21),(19,20),(20,20),(20,19),(21,19),(22,18),]

# green shadow stem
shadowStem = [(10,32),(11,32),(11,31),(11,30),(11,27),(12,27),(11,26),(12,26),(13,26),(11,25),(13,25),(14,25),(12,24),(14,24),(13,23),(12,22),(13,22),(14,22),(15,22),(16,22),(17,22)]

for point in greenPoints:
    im.putpixel(point, stemColor)

for point in shadowStem:
    im.putpixel(point, stemShade)

# stem style 2
# stem style 3

# add flowers
# flower style 1
centerColor = (255, 252, 158)
innerPetal = (255, 194, 241)
outerPetal = (255, 255, 255)

flowerCenters = [(10,15),(13,13),(13,17),(17,14),(17,18),(21,16)]
innerPetals = [(10,14),(10,16),(11,15),(9,15),
(13,14),(13,12),(12,13),(14,13),
(13,18),(13,16),(12,17),(14,17),
(17,13),(17,15),(16,14),(18,14),
(17,17),(17,19),(16,18),(18,18),
(21,15),(21,17),(20,16),(22,16)]

outerPetalsF1 = [
(10,13),(11,13),(11,14), #top   
(10,17),(9,17),(9,16),#bottom 
(12,15),(12,16),(11,16),#right
(8,15),(8,14),(9,14), #left
]

flower0 = []
flower1 = []
flower2 = []
flower3 = []
flower4 = []
flower5 = []

# (10,15)
flowers = [flower0,flower1,flower2,flower3,flower4,flower5]
petal =[]
flowerCounter = 0
for (i, j) in flowerCenters:
    print("(I, J)")
    print(i,j)
    # print("flower" + str(flowerCounter))
    # flower = "flower" + str(flowerCounter)
    # for flower in flowers:
    flower.append((i,j-2)) #(10,13)
    flower.append((i+1,j-2)) #(11,13)
    flower.append((i+1,j-1)) #(11,14)
    flower.append((i,j+2)) #(10,17)
    flower.append((i-1,j+2)) #(9,17)
    flower.append((i-1,j+1)) #(9,16)
    flower.append((i+2,j)) #(12,15)
    flower.append((i+2,j+1)) #(12,16)
    flower.append((i+1,j+1)) #(11,16)
    flower.append((i-2,j)) #(8,15)
    flower.append((i-2,j-1)) #(8,14)
    flower.append((i-1,j-1)) #(9,14)

    # break
    # print(flower)
    # flowerCounter = int(flowerCounter)
    # flowerCounter+=1

        

for center in flowerCenters:
    im.putpixel(center, centerColor)

for inner in innerPetals:
    im.putpixel(inner, innerPetal)

for p in petal:
    im.putpixel(p, outerPetal)
border()
# sprinkles()
im.show()