import textwrap

def wrap(string, max_width):
    text = textwrap.fill(string, max_width)
    #print(textwrap.fill(string, max_width)) -> ABCD \n EFGH
    #print(textwrap.wrap(string, max_width)) -> ['ABCD', 'EFGH']
    return text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)