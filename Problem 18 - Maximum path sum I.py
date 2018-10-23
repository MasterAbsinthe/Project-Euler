# Euler Project, problem 18
# By Espen Sales
# 04/10/2018

trilis = [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

paths = [[0]]


for x in range(1,len(trilis)):     # Generates sequences representing the possible routes
    for y in range(0,len(paths)):
        paths.append(list(paths[y]))
        paths[y].append(paths[y][len(paths[y])-1]+1)
        paths[len(paths)-1].append(paths[len(paths)-1][len(paths[len(paths)-1])-1])
        print(paths[len(paths)-1])
        
maxsum = 0

for x in range(0,len(paths)):    # The sum of all routes is calculated by applying the corresponding values of the triangle to the corresponding digits of the generated sequences (representing all routes). The greatest sum, represented by the variable "maxsum", is found. 
    sum=0
    for y in range(0,len(paths[0])):
        sum += trilis[y][paths[x][y]]
    if sum > maxsum:
        maxsum = sum
    print(x,"of",str(len(paths))+", current sum:",str(sum)+", maximum sum:", maxsum)

print()
print("The greatest sum of a route is",maxsum)


    