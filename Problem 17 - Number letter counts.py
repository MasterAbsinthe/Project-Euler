# Euler Project, problem 17
# By Espen Sales
# 04/10/2018

def prout(n):              # Function "prout" takes a natural number "k" between 1 and 1000 and outputs the number written out in words
    def transsingle(k):    
        if k == 0:
            return ""
        if k == 1:
            return "one"
        if k == 2:
            return "two"
        if k == 3:
            return "three"
        if k == 4:
            return "four"
        if k == 5:
            return "five"
        if k == 6:
            return "six"
        if k == 7:
            return "seven"
        if k == 8:
            return "eight"
        if k == 9:
            return "nine"
            
    def transteen(k):
        if k == 0:
            return "ten"
        if k == 1:
            return "eleven"
        if k == 2:
            return "twelve"
        if k == 3:
            return "thirteen"
        if k == 4:
            return "fourteen"
        if k == 5:
            return "fifteen"
        if k == 6:
            return "sixteen"
        if k == 7:
            return "seventeen"
        if k == 8:
            return "eighteen"
        if k == 9:
            return "nineteen"
            
    def transdouble(k):
        if k == 0:
            return ""
        if k == 2:
            return "twenty"
        if k == 3:
            return "thirty"
        if k == 4:
            return "forty"
        if k == 5:
            return "fifty"
        if k == 6:
            return "sixty"
        if k == 7:
            return "seventy"
        if k == 8:
            return "eighty"
        if k == 9:
            return "ninety"
        
    numlis = [i for i in str(n)]
    
    if len(numlis) == 1:
        nom = transsingle(int(numlis[0]))
    
    if len(numlis) == 2:
        if numlis[0] == "1":
            nom = transteen(int(numlis[1]))
        if numlis[0] != "1":
            nom = transdouble(int(numlis[0]))
            nom += "-"+transsingle(int(numlis[1]))
     
    if len(numlis) == 3:
        nom = transsingle(int(numlis[0]))+" hundred"
        if numlis[1] != "0" or numlis[2] != "0":
            nom += " and "
        
        if numlis[1] == "1":
            nom += transteen(int(numlis[2]))
        if numlis[1] != "1":
            nom += transdouble(int(numlis[1]))
            if numlis[1] != "0" or numlis[2] != "0":
                nom += "-"
            nom += transsingle(int(numlis[2]))
            
    if len(numlis) == 4:
        nom = "one thousand"  
                 
    return nom
    
ans = 0

for x in range(1,1001):    # Function "prout" is summoned to write out numbers 1 to 1000 as strings, spaces and hypens are removed, length of string is counted, length of string is added to variable "ans" which represents the final answer.  
    num = prout(x)
    num = num.replace(" ","")
    num = num.replace("-","")
    ans += len(num)
    print()
    print(prout(x),"-",num,"-",len(num),"-",ans)

print()
print("The number of letters used when printing out numbers 1 to 1000 is",ans)
    
    