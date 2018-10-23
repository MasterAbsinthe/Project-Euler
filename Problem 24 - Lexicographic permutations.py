# Project Euler, Problem 24.
# By Espen Sales
# 18/10/2018

pernu = ["0","1","2","3","4","5","6","7","8","9"]    # List of digits to be permuted
permu = pernu                                        # List that will contain permutations, starts as the digits to be permuted
amonu = len(pernu)    # Final length of permutations
goalp = 1000000       # The final placement for the lexicographic permutation to be found

def pergen(n):                  # Takes list of digits n and returns list with all permutations in lexiconological order
    for x in range(0,amonu-1):
        q = []
        for x in range(0,len(n)):
            for y in range(0,len(pernu)):
                if str(y) not in n[x]:
                    q.append(n[x]+str(y))
                    print(n[x]+str(y), len(n[x]+str(y)))
        n = q
    return(n)
    
permu = pergen(permu)
    
print("The",str(goalp)+"th permutation of numbers",pernu,"is",permu[goalp-1])

