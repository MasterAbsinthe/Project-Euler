# Project Euler, Problem 2.
# By Espen Sales
# 17/09/2018

t1 = 2
t2 = 1
sum = 2
t=1

while t <= 4000000:
    t = t1+t2
    if t%2 == 0:
        sum += t
        print(sum)
    t1 = t
    t2 = t - t2
