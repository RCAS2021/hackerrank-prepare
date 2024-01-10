def diagonalDifference(arr):
    prim_diag = 0
    sec_diag = 0
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i == j):
                prim_diag += arr[i][i]

    reverse_array = list(reversed(arr))

    for i in range(len(reverse_array)):
        sec_diag += reverse_array[i][i]

    print(abs(prim_diag - sec_diag))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)