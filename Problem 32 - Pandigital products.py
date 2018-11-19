# Project Euler, problem 32
# By Espen Sales
# 01/11/2018

pangit = [str(x) for x in range(1,10)]    # List of numbers from 1 through 9
maip = 10000                              # Multipliers or multiplicants exceeding this will not result in a multiplicand/multiplier/product identity pandigitality
luppi = []      # List of unusual products with multiplicand/multiplier/product identity pandigitality

for x in range(0,maip):
    print(x,maip)
    for y in range(0,maip):
        if sorted(str(x)+str(y)+str(x*y)) == pangit:
            luppi.append(int(x*y))

print()
print("There are a total of",len(luppi),"1 through 9 pandigital multiplicant/multiplier/product identities, the sum of the products of these identities with no repetitions is",sum(set(luppi)))
            