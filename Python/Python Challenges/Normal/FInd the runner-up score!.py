if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) #make list
    arr.sort() #sort list
    arr = list(set(arr)) #remove duplicates

    print(arr[-2]) #EX: [0, 1, 2] -> goes 0(0) -> -1(2) -> -2(1)