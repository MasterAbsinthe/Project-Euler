# Project Euler, Problem 23.
# By Espen Sales
# 17/10/2018

abulis = []    # The list which will hold all abundant numbers smaller than the "limit" value
limit = 28123    # All integers greater than this limit can be written as the sum of two abundant numbers
smabu = 12       # The smallest abundant number
sumbu = 24    # The smallest number that can be written as the sum of two abundant numbers

def sist(n):     # This function determines the sum of all proper divisors of n that are smaller than n.
    dist = []
    for x in range(1,n):
        if n%x==0:
            dist.append(x)
    return sum(dist)
    
for x in range(smabu,limit+1):    # This loop generates all abundant numbers no greater than the "limit" value, which are added to list "abulis"
    if x < sist(x):
        abulis.append(x)
        print(x)

sumnu = 0    # The sum of all positive integers no greater than the "limit" value

for x in range(1,limit+1):
    sumnu += x
    
sudisu = []    # This will hold all numbers that can be written as the sum of two abundant numbers

for x in range(0,len(abulis)):        # This loop generates the numbers that can indeed be written as the sum of two abundant numbers
    for y in range(x,len(abulis)):
        if abulis[x]+abulis[y] <= limit:
            sudisu.append(abulis[x]+abulis[y])
    print(x)

sudiset = set(sudisu)     # Converting the list of numbers into a set will remove any duplicates


print("The sum of all integers that do not exceed",limit,"and cannot be written as a sum of two abundant numbers is",sumnu-sum(sudiset))






    