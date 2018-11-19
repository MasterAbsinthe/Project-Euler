# Project Euler, problem 36
# By Espen Sales
# 07/11/2018

def Pali_Deci(n):    # Determines if n is a palindrome in base ten
    checklength = int(((len(str(n))/2)//1))
    for x in range(0,checklength):
        if str(n)[x] != str(n)[len(str(n))-1-x]:
            return False
    return True

    
def Pali_Bina(n):    # Determines if n is a palindrome in base two
    binary = str(bin(n))[2:]
    checklength = int(((len(str(binary))/2)//1))
    for x in range(0,checklength):
        if str(binary)[x] != str(binary)[len(binary)-1-x]:
            return False
    return True

maxvalue = 1000000    # Double-base palindromes will be found up to but not including this value
pali_sum = 0          # Sum of double-base palindrmes under "maxvalue" value


for x in range(0,maxvalue):
    if Pali_Deci(x) == True and Pali_Bina(x) == True:
        print(x)
        pali_sum += x

print()        
print("The sum of all numbers, less than",str(maxvalue)+", which are palindromic in base 10 and base 2 is",pali_sum)