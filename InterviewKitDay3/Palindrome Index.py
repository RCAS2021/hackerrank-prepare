def palindromeIndex(s):
    teste = []

    for i in range(len(s)):
        if(s[i] == s[len(s)-i-1]):
            teste.append(True)
        else:
            if s[i+1] == s[-i-1]:
                return i
            elif s[-i-2] == s[i]:
                return  len(s)-i-1
    if(all(teste) == True):
        return -1         

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        print(result)
