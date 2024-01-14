# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

#Without recursion
#def superDigit(n, k):
#    p = list(n)
#    
#    for i in range(len(p)):
#        p[i] = int(p[i])
#        
#    s = sum(p)
#    s *= k
#
#    while (s > 9):
#        p = str(s)
#        p = list(p)
#        for i in range(len(p)):
#            p[i] = int(p[i])
#        s = sum(p)
#    return s

#With recursion
def superDigit(n, k):
    p = list(n)
    
    for i in range(len(p)):
        p[i] = int(p[i])
        
    s = sum(p)
    s *= k

    while (s > 9):
        s = superDigit(str(s), 1)
    return s

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)