# Project Euler, Problem 28.
# By Espen Sales
# 23/10/2018

spino = [1]    # Holds the numbers that have been placed
spili = []

silen = 1001                # Final length of spiral
splay = int((silen-1)/2)    # Amount of layers in final spiral

for x in range(0,silen):
    spili.append([])
    for y in range(0, silen):
        spili[x].append(0)
        
spili[int((silen/2)-0.5)][int((silen/2)-0.5)] = spino[0]

for x in range(1,splay+1):      # generates the spiral grid.
    # x equals current layer
    for y in range(0,4):
        # y equals direction of single path, 0 = down, 1 = left, 2 = up, 3 = right
        dirle = x*2
        for z in range(0,dirle):
            if y == 0:
                spili[int((silen/2)-0.5)-(x-1)+z][int((silen/2)-0.5)+x] = spino[len(spino)-1]+1
                spino.append(spino[len(spino)-1]+1)
            if y == 1: 
                spili[int((silen/2)-0.5)+x][int((silen/2)-0.5)+(x-1)-z] = spino[len(spino)-1]+1
                spino.append(spino[len(spino)-1]+1)
            if y == 2:
                spili[int((silen/2)-0.5)+(x-1)-z][int((silen/2)-0.5)-x] = spino[len(spino)-1]+1
                spino.append(spino[len(spino)-1]+1)
            if y == 3:
                spili[int((silen/2)-0.5)-x][int((silen/2)-0.5)-(x-1)+z] = spino[len(spino)-1]+1
                spino.append(spino[len(spino)-1]+1)
        print(spino[len(spino)-1],"of",silen*silen)

diagosu = 0

for x in range(0,silen):      # Calculates sum of diagonal digits
    diagosu += spili[x][x]
    if x != int((silen/2)-0.5):
        diagosu += spili[len(spili)-1-x][x]

print()
for x in range(0,silen):
    print(spili[x])

print()
print("The sum of the numbers on the diagonals in a",silen,"by",silen,"spiral is",diagosu)