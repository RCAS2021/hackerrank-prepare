def flippingMatrix(matrix):
    length = len(matrix)//2
    arr = []
    for i in range(length):
        for j in range(length):
            temp = []
            temp.append(matrix[i][j])
            temp.append(matrix[i][2*length-j-1])
            temp.append(matrix[2*length-i-1][j])
            temp.append(matrix[2*length-i-1][2*length-j-1])
            arr.append(max(temp))

    print(sum(arr))

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)