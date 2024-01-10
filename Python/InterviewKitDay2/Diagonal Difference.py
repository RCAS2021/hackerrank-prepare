def diagonalDifference(arr, n):
    sumA = 0
    sumB = 0
    for i in range(n):
        for j in range(n):
            if(i == j):
                sumA += arr[i][j]

    i = 0
    j = n-1
    
    for _ in range(n):
        sumB += arr[i][j]
        i+=1
        j-=1

    print(abs(sumA - sumB))
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr, n)