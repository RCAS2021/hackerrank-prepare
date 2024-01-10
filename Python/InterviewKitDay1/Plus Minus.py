def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    length = len(arr)
    
    for i in range(length):
        if(arr[i] > 0):
            pos += 1
        elif(arr[i] < 0):
            neg += 1
        else:
            zero += 1

    print(f"{pos/length:.6f}")
    print(f"{neg/length:.6f}")
    print(f"{zero/length:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)