def maxMin(operations, x):
    arr = []
    for i in range(len(x)):
        if(operations[i] == "push"):
            arr.append(x[i])
        elif(operations[i] == "pop"):
            arr.remove(x[i])
        print(min(arr) * max(arr))


if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    result = maxMin(operations, x)