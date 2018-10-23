# Project Euler, Problem 10.
# By Espen Sales
# 25/09/2018

n=1
prist=[2,3]

while (6*n-1) < 2000000:
    for x in range(0,round(len(prist)/5)+1):
        if (6*n-1)%prist[x]==0:
            break
        if x==round(len(prist)/5):
            prist.append((6*n-1))
    for x in range(0,round(len(prist)/5)+1):
        if (6*n+1)%prist[x]==0:
            break
        if x==round(len(prist)/5):
            if (6*n+1) < 2000000:
                prist.append((6*n+1))
    n += 1
    if n%1000==0:
        print(6*n+1)
    
print(sum(prist))