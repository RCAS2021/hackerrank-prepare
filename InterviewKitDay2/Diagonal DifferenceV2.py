def diagonalDifference(arr, n):
    sumA = 0
    sumB = 0
    for i in range(n): sumA += arr[i][i] #arr[0,0], arr[1,1], arr[2,2]...
    
    for i in range(n): sumB += arr[i][n-1-i] #arr[0,2(3-1-0)], arr[1,1(3-1-1)], arr[2,0(3-1-2)]...

    print(abs(sumA - sumB))
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr, n)