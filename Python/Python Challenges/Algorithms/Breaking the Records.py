def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    count_max = 0
    count_min = 0
    
    for i in range(len(scores)):
        if (scores[i] > max_score):
            max_score = scores[i]
            count_max += 1
        if (scores[i] < min_score):
            min_score = scores[i]
            count_min +=1
            
    print(count_max, count_min, sep=" ")

if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)