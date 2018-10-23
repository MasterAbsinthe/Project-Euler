# Project Euler, Problem 19.
# By Espen Sales
# 08/10/2018

månli = []

år = 1900

while True:      # Creates list "månli" where each item represents what month each day of the twentieth century coincided with, including the year 1900.
    print(år)
    for x in range(0,31):
        månli.append("Jan")
    if år%4==0:
        if år%100!=0:
            for x in range(0,29):
                månli.append("Feb")
        elif år%100==0:
            if år%400==0:
                for x in range(0,29):
                    månli.append("Feb")
            else:
                for x in range(0,28):
                    månli.append("Feb")
    else:
        for x in range(0,28):
            månli.append("Feb")
    for x in range(0,31):
        månli.append("Mar")
    for x in range(0,30):
        månli.append("Apr")
    for x in range(0,31):
        månli.append("Mai")
    for x in range(0,30):
        månli.append("Jun")
    for x in range(0,31):
        månli.append("Jul")
    for x in range(0,31):
        månli.append("Aug")
    for x in range(0,30):
        månli.append("Sep")
    for x in range(0,31):
        månli.append("Oct")
    for x in range(0,30):
        månli.append("Nov")
    for x in range(0,31):
        månli.append("Dec")
    år +=1
    if år == 2001:
        break

dagli = []

while True:              # Creates list "dagli" where each item represents what weekday each day of the twentieth century was, including the year 1900.
    print(len(dagli))
    dagli.append("Mon")
    if len(dagli)==len(månli):
        break
    dagli.append("Tue")
    if len(dagli)==len(månli):
        break
    dagli.append("Wed")
    if len(dagli)==len(månli):
        break
    dagli.append("Thu")
    if len(dagli)==len(månli):
        break
    dagli.append("Fri")
    if len(dagli)==len(månli):
        break
    dagli.append("Sat")
    if len(dagli)==len(månli):
        break
    dagli.append("Sun")
    if len(dagli)==len(månli):
        break

Suco = 0
    
for x in range (364,len(månli)):                   # Each day in the twentieth century (here excluding the year 1900) is checked for being a Sunday and also being the first of the month. For each day where this holds true, variable "Suco" is increased by one, meaning it will represent the total of sundays in the twentieth century that fall on the first of the month 
    if dagli[x]=="Sun" and månli[x]!=månli[x-1]:
        Suco += 1
    print(Suco)
    
print("There were a total of",Suco,"sundays that fell on the first of a month during the twentieth century!")


    




























    

