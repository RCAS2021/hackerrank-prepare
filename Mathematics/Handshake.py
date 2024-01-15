import math
#
# Complete the 'handshake' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def handshake(n):
    # return math.factorial(n) // (2 * math.factorial(abs(n - 2))) <= combination without repetition formula
    return math.comb(n, 2)
    
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = handshake(n)