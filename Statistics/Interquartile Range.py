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
        return (arr[len(arr)//2-1] + arr[len(arr)//2]) /2
        
def interQuartile(values, freqs):
    S = []
    for i in range(len(values)):
        for _ in range(freqs[i]):
            S.append(values[i])
    
    S.sort()
    
    arrQ1 = []
    arrQ3 = []
    half = math.floor(len(S)/2)
    for i in range(0, half):
        arrQ1.append(S[i])
    if (isEven(len(S)) == 0):
        for i in range(half+1, len(S)):
            arrQ3.append(S[i])
    else:
        for i in range(half, len(S)):
            arrQ3.append(S[i])
            
    Q1 = median(arrQ1)
    Q3 = median(arrQ3)
    print(f"{Q3-Q1:.1f}")


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)