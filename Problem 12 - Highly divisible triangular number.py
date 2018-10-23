# Project Euler, Problem 12.
# By Espen Sales
# 25/09/2018

num = 0
x = 1
biglength = 0

while True:
    num += x
    faclis=[]
    for y in range(1,round((num+1)/2)+1):
        if num%y==0:
            faclis.append(y)
    faclis.append(num)
    if len(faclis)>biglength:
        biglength = len(faclis)
    if len(faclis)>=500:
        break
    x +=1
    #print(biglength)
    print(num)
    print(biglength)

print(str(num)+":",faclis)

            
            

