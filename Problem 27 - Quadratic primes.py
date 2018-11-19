# Project Euler, Problem 27.
# By Espen Sales
# 23/10/2018

bipri = -1

for a in range(-999,999):
    for b in range(-1000,1001):
        n = 0                      # n is equal to the number of primes the particular mix of a and be yields
        while True:
            if (n**2)+a*n+b > 1 or (n**2)+a*n+b < -1:
                for x in range(2,round((abs((n**2)+a*n+b)+4)/2)):
                    if (abs((n**2)+a*n+b))%x==0:
                        prino = False
                        break
                    if x == round((abs((n**2)+a*n+b)+1)/5):
                        prino = True 
            else:
                prino == False
            if prino == False:
                break
            n += 1
        if n > bipri:
            bipri = n
            coefa = a
            coefb = b
        print(a,b,n,bipri)

print()
print("The product of the coefficients, a and b, for the quadratic expression n^2+a*n+b that produce the maximum number of primes for consecutve values of n, starting with n=0 is",coefa*coefb,"where a ="+str(coefa),"and b ="+str(coefb)+", which yields",bipri,"consecutive prime numbers")
            