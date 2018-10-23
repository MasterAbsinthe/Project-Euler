# Project Euler, Problem 5.
# By Espen Sales
# 21/09/2018

trulis=[]
num=20

while True:
    for x in range(1,20):
        if num%(20-x) != 0:
            trulis=[]
            break
        if num%(20-x) == 0:
            print(num)
            trulis.append(0)
    if len(trulis)== 19:
        break
    num+=20

print()
print(num,"er det minste tallet delig på alle naturlige tall fra 1 til og med 20, gratulerer!")
    
    