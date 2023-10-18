def count_substring(string, sub_string):
    
    cont = 0
    for ss in range(len(string)):
        if(string[ss:ss + len(sub_string)] == sub_string):
            cont += 1
    return cont

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)