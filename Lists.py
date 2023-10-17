if __name__ == '__main__':
    N = int(input())                                     #Actions quantity
    lista = list()                                       #Create empty list
    for _ in range(N):
        option = input().split()                         #Gets option and values, split by a space EX: insert 0 5

        if(option[0] == "insert"):                       #Gets the value in position 0 and compares
            lista.insert(int(option[1]), int(option[2])) #Uses insert built_in function to insert a value(defined by option[2]) in a given position of the list(defined by option[1])
        
        if(option[0] == "print"):
            print(lista)                                 #Prints the list
        
        if(option[0] == "remove"):
            remove = int(option[1])                      #Gets the value to be removed in the given position(defined by option[1])
            lista.remove(remove)                         #Removes the first ocurrence of the given value using the built_in function remove
        
        if(option[0] == "append"):
            append = int(option[1])                      #Gets the value to be appended(inserted at the end of the list) in the given position(defined by option[1])
            lista.append(append)                         #Inserts value at the end of the list using built_in function append
        
        if(option[0] == "sort"):
            lista.sort()                                 #Sorts the values using the built_in function sort
        
        if(option[0] == "pop"):
            lista.pop()                                  #Removes last element of the list using built_in function pop
        
        if(option[0] == "reverse"):
            lista.reverse()                              #Reverses the list using built_in function reverse