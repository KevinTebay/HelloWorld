artists,songs = (10,10)
A = ['a','b','c','d','e','f','g','h','i','j']

playlist = [[0 for j in range(10)] for i in range(10)]
playlist[1][1] = A[0]+"1"

for r in range(10):
    for c in range(10):
        playlist[r][c] = str(r)+str(c)


print(playlist)
