def palindromeIndex(s):
    if(s == s[::-1]):
        return -1

    for i in range((len(s)//2) + (len(s)%2)):
        if s[i] != s[-i-1]:
            if s[i+1] == s[-i-1]:
                return i
            elif s[-i-2] == s[i]:
                return  len(s)-i-1
    
if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        print(result)