if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    highest = -63
    
    for i in range(4):
        for j in range(4):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sum_ = top + middle + bottom
            
            if sum_ > highest:
                highest = sum_
    print(highest)