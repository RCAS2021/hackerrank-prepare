def subsetA(arr):
    arr.sort()
    A = []
    sumA = 0
    sumB = 0
    
    B = []
    for i in range(0, len(arr)):
        B.append(arr[i])
        sumB += arr[i]
        
    for i in range(0, len(arr)):
        if (sumA < sumB):
            popped = B.pop()
            A.append(popped)
            sumA += popped
            sumB -= popped
    A.reverse()
    print(*A, sep="\n")
            
if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)