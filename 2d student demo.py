scores = [[90, 85, 88],[78, 92, 87],[85, 80, 91],[88, 94, 89]]

for i in range (len(scores)):
    for j in range(len(scores[i])):
        print("Student " + str(i+1) + ", Subject " + str(j+1) + ": " + str(scores[i][j]))
        
