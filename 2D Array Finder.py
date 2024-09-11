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

while True:
    x = random.randint(0,4)
    y = random.randint(0,4)
    keypart=""
    checkarray=""
    xandy.clear()
    print("\nYour current score is ",score)
    print("\nYour array is called array2d")
    print("Please type in the command to print the array number",array2d[x][y])
    checkarray = input("Type in command:")
    for i in checkarray:
        if i == "[":
            gi = True
        elif i == "]":
            gi = False
        if gi == True:
            keypart += i
    xandy = keypart.split("[")
    if xandy[1] == str(x):
        print("1st part correct")
        score += 5
    else:
        print("It should have been","[",x,"]")
    if xandy[2] == str(y):
        print("2nd part correct")
        score += 5
    else:
        print("It should have been","[",y,"]")
