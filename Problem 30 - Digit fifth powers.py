# Project Euler, Problem 30.
# By Espen Sales
# 25/10/2018

subermsud = []

for x in range(10,10000000):
    if sum(list([int(i)**5 for i in str(x)])) == x:
        subermsud.append(x)

print()
print("The sum of all the numbers that can be written as the sum of fifth powers of their digits is",sum(subermsud))