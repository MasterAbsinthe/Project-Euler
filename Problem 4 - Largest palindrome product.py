# Project Euler, Problem 4.
# By Espen Sales
# 21/09/2018
done=False
palist=[]

for x in range(901,1000):
    for y in range(901,1000):
        if len(str((1000-(x-900))*(1000-(y-900)))) == 6:
            digits = [int(i) for i in str((1000-(x-900))*(1000-(y-900)))]
            if digits[0] == digits[5]:
                if digits[1] == digits[4]:
                    if digits[2] == digits[3]:
                        print()
                        print((1000-(x-900)),"*",(1000-(y-900)),"=",(1000-(x-900))*(1000-(y-900)))
                        print("Dette er en palindrom!")
                        palist.append(int((1000-(x-900))*(1000-(y-900))))
                    else:
                        continue
                else:
                    continue
            else:
                continue
        if 1000-y == 1:
            break
    if 1000-x == 1:
        break

print()
print("Det høyeste palindrom er herved",str(max(palist))+". Gratulerer!")