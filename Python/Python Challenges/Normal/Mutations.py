#Change a string's character in a given position
def mutate_string(string, position, character):
    l = list(string) #transform the string to a list
    l[position] = character #change the character in the given position
    strr = ''.join(l) #join the list to form a string: ['a','b',...] -> ab...
    return strr

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)