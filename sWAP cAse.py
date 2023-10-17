def swap_case(s):
    s1 = ""
    for char in s:
        if char.isupper():
            s1 += char.lower()
        else:
            s1 += char.upper()
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)