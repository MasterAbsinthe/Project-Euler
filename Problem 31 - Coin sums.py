# Project Euler, Problem 31.
# By Espen Sales
# 25/10/2018

valuli = [1,2,5,10,20,50,100,200]    # List of coin values in pence exclusively
coms = [[1],[2],[5],[10],[20],[50],[100],[200]]    # List of coin combinations
faums = []    # Secondary list of coin combinations
noms = []    # combinations that total 200 pence


while True:
    for x in range(0,len(coms)):
        if sum(coms[x]) >= 200:
            if sum(coms[x]) == 200:
                noms.append(coms[x])
                print(len(noms), len(coms))
        else:
            for y in range(0,len(valuli)):
                faums.append(list(coms[x]))
                faums[len(faums)-1].append(int(valuli[y]))
    if faums == []:
        break
    coms = faums
    faums = []

for x in range(0,len(noms)):
    noms[x].sort
    noms[x]=[str(i) for i in noms[x]]
    noms[x]="".join(noms[x])
    print(x,len(noms))

print(len(set(noms)))


        
            
        