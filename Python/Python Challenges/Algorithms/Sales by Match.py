def sockMerchant(n, ar):
    pair = 0
    unique_num = set(ar)
    for i in unique_num:
        pair += ar.count(i)//2
    print(pair)

if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)