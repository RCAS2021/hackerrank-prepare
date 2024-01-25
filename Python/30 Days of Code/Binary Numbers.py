if __name__ == '__main__':
    n = int(input().strip())
    n = str(bin(n)[2:])
    count = 0
    count_max = 0
    for i in n:
        if i == '1':
            count += 1
            count_max = max(count, count_max)
        else:
            count = 0
    print(count_max)