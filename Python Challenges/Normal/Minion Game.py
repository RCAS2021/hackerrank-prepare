#Explanation:

#robotc142 7 years ago
#Let me put an example here to further illustrate the idea:

#For the word "BANANA", the first vowel 'A' occurs at position 1, len("BANANA") = 6, so there are 6-1 = 5 
#substrings starting with this letter 'A': ['A', 'AN', 'ANA', 'ANAN', 'ANANA'], you add one extra letter to 
#that specific letter 'A' until you get to the end of the word.

def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    vowels = ["A","E","I","O","U"]

    for i in range(len(string)):
        if(string[i] in vowels):
            kevin_score += len(string)-i
            print(f"The {i+1} letter {string[i]} has {len(string)-i} possible combinations")
            
        else:
            stuart_score += len(string)-i
            print(f"The {i+1} letter {string[i]} has {len(string)-i} possible combinations")
            
    
    print("Kevin score: ", kevin_score)
    print("Stuart score: ", stuart_score)

    if (stuart_score > kevin_score):
        print(f"Stuart {stuart_score}")
    elif(kevin_score > stuart_score):
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)