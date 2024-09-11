# 2D array representing student grades
# Each row corresponds to a student, and each column represents a subject
scores = [
    [90, 85, 88],
    [78, 92, 87],
    [85, 80, 91],
    [88, 94, 89]
]

# Accessing individual elements
# print("Grade of student 2 in subject 3: " + str(grades[1][2]))

# Iterating through the 2D array
for i in range(len(scores)):
    for j in range(len(scores[i])):
        print("Student " + str(i + 1) + ", Subject " + str(j + 1) + ": " + str(scores[i][j]))
