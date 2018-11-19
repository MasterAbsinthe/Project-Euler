# Project Euler, problem 31
# By Espen Sales
# 01/11/2018

import matplotlib.pyplot as plt

valuli = [1,2,5,10,20,50,100,200]
dessu = 200
coms = [[n] for x,n in enumerate(valuli)]
foms = []
noms = []

comsx = [1]
comsy = [0]

while True:
    comsx.append(int(comsx[len(comsx)-1]+1))
    comsy.append(int(len(coms)))
    
    for x in range(len(coms)):
        if sum(coms[x]) >= dessu:
            if sum(coms[x]) == dessu:
                noms.append(list(coms[x]))
                print(len(noms),len(coms))
                
        else:
            for y in range(len(valuli)):
                    foms.append(list(coms[x]))
                    foms[len(foms)-1].append(int(valuli[y]))
    if foms == []:
        break
    
    foms = [sorted(s) for s in foms]
    foms = [tuple(t) for t in foms]
    foms = set(foms)
    foms = [list(l) for l in foms]
    coms = foms
    foms = []
    

noms = [sorted(s) for s in noms]
noms = [tuple(t) for t in noms]
noms = set(noms)
noms = [list(l) for l in noms]

plt.plot(comsx,comsy)
plt.xlabel("iterations")
plt.ylabel("number of combinations totalling under or equal to 200")
plt.grid(True)
plt.show

print("There are a total of",len(noms),"combinations")

