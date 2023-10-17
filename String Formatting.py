def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range (1, number+1):
        print(str(i).rjust(width)+oct(i)[2:].rjust(width+1)+hex(i)[2:].upper().rjust(width+1)+bin(i)[2:].rjust(width+1))
    
    print(bin(number))
    print(oct(number))
    print(hex(number))

    print(bin(number)[2:])
    print(oct(number)[2:])
    print(hex(number)[2:])

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)