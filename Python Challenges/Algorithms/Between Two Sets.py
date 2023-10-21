def getTotalX(a, b):
    count = 0
    for i in range(1, max(b)+1):
        if ((all(i % j == 0 for j in a)) and (all(j % i == 0 for j in b))):
            count += 1
            
    print(count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)