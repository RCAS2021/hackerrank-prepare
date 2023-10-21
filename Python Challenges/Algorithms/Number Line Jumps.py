def kangaroo(x1, v1, x2, v2):
    test = "NO"
    for i in range(10000):
        if((x1 + v1) == (x2 + v2)):
            test = "YES"
        else:
            x1 += v1
            x2 += v2
    print(test)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)