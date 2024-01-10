def split_and_join(line):
    tf = line.split()
    tf = "-".join(tf)
    return tf

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)