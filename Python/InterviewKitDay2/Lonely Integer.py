def lonelyinteger(a):
    if(len(a) == 1):
            print(*a)
    else:
        for i in a:
            if(a.count(i) == 1):
                print(i)

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)