def miniMaxSum(arr):
    arr.sort()
    mini = 0
    maxi = 0
    for i in range(0, len(arr)-1):
        mini += arr[i]
    for i in range(1, len(arr)):
        maxi += arr[i]
    
    print(mini, maxi, end=" ")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)