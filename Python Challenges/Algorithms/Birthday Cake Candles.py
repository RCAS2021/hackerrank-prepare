def birthdayCakeCandles(candles):
    highest = max(candles)
    total = 0
    
    for i in range(len(candles)):
        if(candles[i] == highest):
            total += 1
    print(total)

if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)