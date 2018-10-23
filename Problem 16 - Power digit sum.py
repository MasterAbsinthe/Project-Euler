# Euler Project, problem 16
# By Espen Sales
# 03/10/2018

bas = 2
pow = 1000
bum = bas**pow
lis = []

for i in str(bum):
    lis.append(int(i))

print()
print("The sum of all digits of",str(bas)+"^"+str(pow),"is",sum(lis))

