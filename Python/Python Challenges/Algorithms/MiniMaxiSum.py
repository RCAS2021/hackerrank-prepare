def miniMaxSum(arr):
    arr.sort()
    print(sum([arr[i] for i in range(len(arr)-1)]), sum([arr[i] for i in range(1, len(arr))]), sep=" ") 
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)