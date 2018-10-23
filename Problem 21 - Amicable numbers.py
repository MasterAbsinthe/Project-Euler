# Project Euler, Problem 21.
# By Espen Sales
# 16/10/2018

max = 10000

def sist(n):     # This function determines the sum of all proper divisors of n that are smaller than n.
    dist = []
    for x in range(1,n):
        if n%x==0:
            dist.append(x)
    return sum(dist)

amilis = []

for x in range(0,max):                         # Checks each number from 1 to maximum value "max" (10000 in the original Euler problem) for amicability. Amicable numbers are added to list "amilis".
    if x == sist(sist(x)) and x != sist(x):
        amilis.append(x)
        print(x)

print("The sum of all amicable numbers no greater than",max,"is",sum(amilis))