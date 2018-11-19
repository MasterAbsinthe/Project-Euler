# Project Euler, problem 33
# By Espen Sales and Trond Ødegård
# 01/11/2018

triff = []    # List of non-trivial fractions

def Kall(c,t):
    if t == 1:
        s = int (c/10)
    else:
        s = c%10
    return s

for x in range(11,99):
    for y in range(x+1,100):
        print(x,y)
        if x%10 != 0 and y%10 != 0:
            for a in range(0,2):
                for b in range(0,2):
                    if str(x)[a] == str(y)[b]:
                        nonx = Kall(x,a)
                        nony = Kall(y,b)
                        if x/y == nonx/nony:
                            triff.append([nonx,nony])

print()                            
print(triff)

numer = 1
denom = 1

for x in range(len(triff)):
    numer *= triff[x][0]
    denom *= triff[x][1]
    
for x in range(1,numer+1):
    if numer%(numer+1-x) == 0 and denom%(numer+1-x) == 0:
        denom = int(denom/(numer+1-x))
        break

print()
print("The denominator of the fraction of the product of all non-trivial fractions given in its lowest common terms is",denom)




            
