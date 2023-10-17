if __name__ == '__main__':
    N = int(input())
    lista = list()
    for _ in range(N):
        option = input().split()

        if(option[0] == "insert"):
            lista.insert(int(option[1]), int(option[2]))
        if(option[0] == "print"):
            print(lista)
        if(option[0] == "remove"):
            remove = int(option[1])
            lista.remove(remove)
        if(option[0] == "append"):
            append = int(option[1])
            lista.append(append)
        if(option[0] == "sort"):
            lista.sort()
        if(option[0] == "pop"):
            lista.pop()
        if(option[0] == "reverse"):
            lista.reverse()