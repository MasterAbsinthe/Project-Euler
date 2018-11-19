# Project Euler, problem 35
# By Espen Sales
# 06/11/2018


primelist = [2,3,5]

def PrimeList(primelist,maxvalue):    # Adds primes to existing list "primelist" up to but not including "maxvalue" value
    if primelist[len(primelist)-1] >= maxvalue:
        return primelist
    if ((primelist[len(primelist)-1]+1)/6)%1 == 0:
        n = int((primelist[len(primelist)-1]+1)/6)
        lowprime = True
    if ((primelist[len(primelist)-1]-1)/6)%1 == 0:
        n = int(((primelist[len(primelist)-1]-1)/6)+1)
        lowprime = False    
    while 6*n-1 < maxvalue:
        if lowprime == False:
            for x in primelist:
                if (6*n-1)%x == 0:
                    break
                if x >= round((6*n-1)/5)+1:
                    primelist.append(6*n-1)
                    break
        if (6*n+1) < maxvalue:
            for x in primelist:
                if (6*n+1)%x == 0:
                    break
                if x >= round((6*n+1)/5)+1:
                    primelist.append(6*n+1)
                    break
        lowprime = False
        n += 1
    
    return primelist


def PrimeCheck(n,primelist):    # Determines if n is a prime using the list of primes "primelist" and function "PrimeList"
    if n == 2:
        return True
    if primelist[len(primelist)-1] < round(n/5)+2:
        PrimeList(primelist,round(n/5)+1)
    for x in primelist:
        if n%x == 0:
            return False
        if x >= round(n/5)+1:
            return True
    return True


def CirclePrimeList(maxvalue):    # Generates a list of potential circular primes under (but not including) value "maxvalue" using list of primes "primelist". Primes longer than one digit do not include digits 0,2,4,5,6 or 8 as these cannot be circular primes
    circlelist = [2,3,5,7]
    digitlist = [0,2,4,5,6,8]
    n = 2
    
    while 6*n-1 < maxvalue:
        for x in digitlist:
            if  str(x) in str(6*n-1):
                break
            if x == digitlist[len(digitlist)-1]:
                if PrimeCheck(6*n-1,primelist) == True:
                    circlelist.append(6*n-1)
        if 6*n+1 < maxvalue:
            for x in digitlist:
                if  str(x) in str(6*n+1):
                    break
                if x == digitlist[len(digitlist)-1]:
                    if PrimeCheck(6*n+1,primelist) == True:
                        circlelist.append(6*n+1)
        n += 1
    return circlelist

def CirclePrimeCheck(n):   # Determines if a prime n is circular
    nlist = [int(x) for x in str(n)]
    
    for x in range(0,len(str(n))-1):
        nlist1 = [nlist[x] for x in range(1,len(nlist))]
        nlist1.append(nlist[0])
        if PrimeCheck(int("".join([str(x) for x in nlist1])),primelist) == False:
            return False
        nlist = nlist1
    return True

circularprimes = []
maxvalue = 1000000

for x in CirclePrimeList(maxvalue):
    if x not in circularprimes:
        if CirclePrimeCheck(x) == True:
            circularprimes.append(x)
            nlist = [int(i) for i in str(x)]
            for i in range(0,len(nlist)-1):
                nlist1 = [nlist[x] for x in range(1,len(nlist))]
                nlist1.append(nlist[0])
                circularprimes.append(int("".join([str(x) for x in nlist1])))
                nlist = nlist1
                
circularprimes = list(set(circularprimes))

print("There are",len(circularprimes),"circular primes under",maxvalue)
    

    
