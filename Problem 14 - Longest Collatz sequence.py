# Euler Project, problem 14
# By Espen Sales
# 30/09/2018


ceil = 100000   # values are not to exceed ceil
chalen = 0

for x in range(1,ceil):
    chalis=[x]
    while True:
        if x%2==0:
            x = x/2
            chalis.append(x)
            if x==1:
                break
        if x%2!=0:
            x = 3*x+1
            chalis.append(x)
            if x==1:
                break
    if len(chalis)>chalen:
        chalen=len(chalis)
        num = chalis[0]
        print(num)
         
print()
print(num,"is the number that does not exceed")
print(ceil,"and generates the longest collatz sequence, that sequence being")
print(chalen,"numbers long")
    
    