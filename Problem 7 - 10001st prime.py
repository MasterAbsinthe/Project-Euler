# Project Euler, Problem 7.
# By Espen Sales
# 21/09/2018

place = 2
num = 3
print("1:   2")
while True:
    for x in range(2,num):
        if num%x == 0:
            num += 1
            break
        if x == num-1:
            print(str(place)+":  ",num)
            place +=1
            num += 1
            break
    if place == 10002:
        break


            
    
    
    
    