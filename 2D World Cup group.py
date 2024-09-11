groups = [["ENG",3,0,0,9,3,9],["WAL",1,1,1,5,3,4], ["USA",1,1,1,4,5,4],["IRN",0,0,0,4,9,0]]

print("      W D L S C P")
for i in range (len(groups)):
    print(i+1,*groups[i])


