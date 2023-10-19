def countingSort(arr):
    cont = [0] * 100 #Creates an array with 0s

    for i in arr:
        cont[i] += 1
    print(*cont)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)