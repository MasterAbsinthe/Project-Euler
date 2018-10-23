# Project Euler, Problem 25.
# By Espen Sales
# 21/10/2018

fibst = [1,1]    # The two first fibonacci numbers
fibin = 2

while True:
    fibin += 1
    fibcu = fibst[0]+fibst[1]
    fibst[0]=fibst[1]
    fibst[1]=fibcu
    print()
    print(str(fibin)+":",fibcu)
    if len(str(fibcu))==1000:
        break
    

