# Project Euler, Problem 26.
# By Espen Sales
# 21/10/2018

import decimal
decimal.getcontext().prec=10000     # longer decimal numbers


decel = 1000
loccy = 0    # The variable representing the longest reccuring cycle
decde = 0

for d in range(1,decel):
    #print(d)
    deccy = 0                                             # The variable representing the reccuring cycle for each value of d
    decno = str(decimal.Decimal(1)/decimal.Decimal(d))    # 1/d is calculated precisely
    decli = []
    for i in str(decno)[2:-1]:    # The decimal digits are added to list
        decli.append(i)
    while len(decli)>0 and decli[0]=="0":    # All digits equal to zero at the start of the decimal list are unimportant and are removed
        del decli[0]
    decst = "".join(decli)    # For visual purposes the list of decimals is joined into a single string
    #print(decst)
    if len(decst)==9999:           # If the list is shorter than this value it has no reccurrent cycle, or rather, a reccuring cycle of zeroes
        for x in range(1,9001):        # This loop determines the reccuring cycle length for the current value of d
            for y in range(1,9001):
                if decst[len(decst)-y] != decst[len(decst)-y-x]:
                    break
                if y == 9000:
                    deccy = x
                    break
            if deccy == x:
                break
    if deccy > loccy:    # For each reccuring cycle that is longer than the current longest reccuring cycle, the value d is stored
        loccy = deccy
        decde = d
    print(d,deccy,loccy)

print()
print("The longest reccuring cycle in a unit fraction 1/d for which d <",decel,"is",loccy,"where d is equal to",decde)
                
                    
        