if __name__ == '__main__':
    records = []
    scores = []
    alph_names = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    
    records.sort(key = lambda x: x[1], reverse = False)

    for i in range(len(records)):
        scores.append(records[i][1])
    
    lowest_score = list(set(scores))
    lowest_score.sort()
    second_lowest_score = lowest_score[1]

    for i in range(len(records)):
        if (records[i][1] == second_lowest_score):
            alph_names.append(records[i][0])
    
    alph_names.sort()
    for i in range(len(alph_names)):
        print(alph_names[i])