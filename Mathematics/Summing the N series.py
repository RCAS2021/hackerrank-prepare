#
# Complete the 'summingSeries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def summingSeries(n):
    #sum_n = 0
    #for i in range(1, n + 1):
    #    sum_n += i ** 2 - (i-1)**2
    #return int((sum_n % (10 ** 9 + 7)))
    return n * n % (10 ** 9 + 7)
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)