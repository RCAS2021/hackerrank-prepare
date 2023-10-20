def palindromeIndex(s):
    tw = []
    teste = []
    no = []
    for i in range(len(s)):
        tw.append(s[i])
    
    for i in range(len(tw)):
        if(tw[i] == tw[len(tw)-i-1]):
            teste.append(True)
        else:
            if s[i+1] == s[-i-1]:
                return i
            elif s[-i-2] == s[i]:
                return  len(s)-i-1
    if(all(teste) == True):
        return -1
    else:
        return no[0]
        
            

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        print(result)
