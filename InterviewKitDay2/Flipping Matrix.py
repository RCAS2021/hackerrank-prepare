def flippingMatrix(matrix):
    length = len(matrix)//2
    result_sum = 0

    for i in range(length):
        for j in range(length):
            result_sum += max(matrix[i][j], matrix[i][(length*2)-j-1], matrix[(length*2)-i-1][j], matrix[(length*2)-i-1][(length*2)-j-1]) 
            print(result_sum)
    print(result_sum)
       

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)