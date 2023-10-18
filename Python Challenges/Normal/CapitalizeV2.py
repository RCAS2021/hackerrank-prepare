def solve(s):
    words = s.split()
    capitalized_words = []
    for i in range(len(words)):
       capitalized_words.append(words[i].capitalize())
    return capitalized_words

if __name__ == '__main__':
    text = solve(input())
    print(*text)