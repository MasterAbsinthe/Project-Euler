# Euler Project, problem 15
# By Espen Sales
# 01/10/2018

binalen = 30           # Length of final sequences
binalis = ["1","0"]    # List of sequences starts with "1" representing movement to the right on the grid and "0" representing movement downwards on the grid

while True:                            # This loop generates all possible binary numbers as long as half the length of the final sequences "binalen". All of these are valid half-paths
    for x in range(0,len(binalis)):
        binalis.append(binalis[x]+"0")
        binalis[x] = binalis[x]+"1"
        print(binalis[x]," ",len(binalis[x])," ",len(binalis))
    if len(binalis[0]) == binalen/2:
        break
    
sumplac = {} 

for x in range(0,int((binalen/2)+1)):    # Variables are generated inside dictionary "sumplac" and represent the endpoints of the half-paths on the grid. On square grids the amount of these endpoints are the length of the sides of the grid plus one.
    sumplac["sum"+str(x)] = 0
    print(len(sumplac))

for x in range(0,len(binalis)):       # The sum of the digits in any given binary sequence previously generated dictates which endpoint it corresponds to. The value of the variable that represents an endpoint is increased by one for each binary sequence that corresponds to that endpoint, thus the value of this variable will be equal to the amount of sequences that end at the corresponding endpoint.
    tot = sum(map(int,binalis[x]))
    sumplac["sum"+str(tot)] += 1
    print(x," ",len(binalis))

ans = 0 
    
for x in range(0,len(sumplac)):        # Each endpoint marks the end of a certain amount of half-paths that start at the top left of the grid, and there are theoretically as many half-paths from that point on to the bottom right of the grid. Therefore the amount of full paths that meet a given endpoint halfway through is the amount of half-paths to that endpoint squared
    ans += sumplac["sum"+str(x)]**2
    print("Answer:",ans)

print()   
print("There are in total",ans,"possible routes in a",str(int(binalen/2))+"*"+str(int(binalen/2)),"grid")
   