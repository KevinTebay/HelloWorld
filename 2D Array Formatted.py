import random
mainarray = []
array2d = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
counter = 0
keypart = ""
gi = False
score = 0
xandy = []

for i in range(10,35):
    mainarray.append(i)
random.shuffle(mainarray)

for j in range(5):
    for i in range(5):
        array2d[j][i] = mainarray[counter]
        counter+= 1

print("Original array\n")
print(array2d)

print("\nYour 2d Array nicely formatted\n")
for i in range(5):
    print(array2d[i])
