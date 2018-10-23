# Project Euler, Problem 5.
# By Espen Sales
# 21/09/2018

sum=0
for x in range(1,101):
    sum += x
sumkvad=sum**2            # Kvadraten av summen
print("Kvadraten av summen",sum,"er",sumkvad)

kvadsum=0
for x in range(1,101):
    kvadsum += x**2       # Summen av kvadratene

print("Summen av kvadratene er",kvadsum)

ans = sumkvad-kvadsum
print()
print(sumkvad,"-",kvadsum,"=",ans)
    
    
    



