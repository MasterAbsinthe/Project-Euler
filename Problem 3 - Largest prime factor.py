# Project Euler, Problem 3.
# By Espen Sales
# 18/09/2018

tall = int(input("Gi meg et heltall, du "))
print()
done = False

for x in range (2,(tall)):
    if tall%x==0:
        for y in range(2,int(tall/x)):
            if (tall/x)%y == 0:
                print("Faktoren",int(tall/x),"er ikke et primtall fordi den kan deles på",y,"som blir",int((tall/x)/y))
                print()
                break
            if y == ((tall/x)-1):
                print("Faktoren",int(tall/x),"er et primtall, den største primtallsfaktoren i",str(tall)+"!")
                done=True
    if done==True:
        break

if done == False:
    print("Dette er et primtall og har dermed ingen faktorer")