import math

def isEven(length):
    if (length % 2 != 0):
        return 0
    else:
        return 1
        
def median(arr):
    if (isEven(len(arr)) == 0):
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2-1] + arr[len(arr)//2]) //2
        
def quartiles(arr):
    arr.sort()
    arrQ1 = []
    arrQ3 = []
    Q2 = median(arr)
    half = math.floor(len(arr)/2)
    for i in range(0, half):
        arrQ1.append(arr[i])
    if (isEven(len(arr)) == 0):
        for i in range(half+1, len(arr)):
            arrQ3.append(arr[i])
    else:
        for i in range(half, len(arr)):
            arrQ3.append(arr[i])
            
    Q1 = median(arrQ1)
    Q3 = median(arrQ3)
    print(Q1)
    print(Q2)
    print(Q3)


if __name__ == '__main__':
    
    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)