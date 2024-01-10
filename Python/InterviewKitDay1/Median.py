n = int(input())

arr = list(map(int, input().split()))
arr.sort()

middle = len(arr)//2
print(arr[middle])