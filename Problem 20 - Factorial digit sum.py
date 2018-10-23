# Project Euler, Problem 20.
# By Espen Sales
# 16/10/2018

tawl = 100
tawr = 1

for x in range(1,tawl+1):
    tawr *= x

liwr = []

for i in str(tawr):
    liwr.append(int(i))
    
print("The sum of the digits in",str(tawl)+"! is",sum(liwr))
    