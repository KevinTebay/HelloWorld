grades = [["Sally",24,32,5],["Simon", 22,22,53], ["Sandra",43,54,23], ["Steve", 23,12,32], ["Sammy", 23,12,32]]

#for i in range (len(grades)):
#    print (*grades[i])


print("Name: ", grades[0][0],
"Score: ", grades[0][1])


grades[0].append(56), grades[1].append(66), grades[2].append(76), grades[3].append(86), grades[4].append(96)

for i in range (len(grades)):
    print(i+1,*grades[i])

grades[0][0] = "Amanda"


for i in range (len(grades)):
    print (i+1,*grades[i])

#print (grades)

#print(grades[1][2])

#grades[1].append(56)

#print (grades)

