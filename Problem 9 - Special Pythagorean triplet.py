# Project Euler, Problem 9.
# By Espen Sales
# 23/09/2018

import math




for a in range(1,1001):
    print("a=",a)
    for b in range(a+1,1001):
        c = math.sqrt(a**2+b**2)
        if a+b+c == 1000:
            break
    c = math.sqrt(a**2+b**2)
    if a+b+c == 1000:
        break

print(a,"+",b,"+",c,"=",a+b+c)
print(a,"*",b,"*",c,"=",a*b*c)