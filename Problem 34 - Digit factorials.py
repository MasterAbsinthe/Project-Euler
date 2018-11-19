# Project Euler, problem 34
# By Espen Sales
# 01/11/2018

def Digifa(a):
    def Facto(a):
        facto = 1
        if a != 0:
            for x in range(1,int(a)+1):
                facto *= x
        return facto
    
    return sum([Facto(x) for x in str(a)])
        
cemas = 9999999
sumas = 0

for x in range(3,cemas):
    print(sumas)
    if Digifa(x) == x: 
        sumas += x 

print("The sum of all numbers which are equal to the sum of the factorial of their digits is",sumas)

        