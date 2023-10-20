a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(pow(a, b) + pow(c, d)) #This result is bigger than 2^63 -1. Hence, it won't fit in the long long int of C++ or a 64-bit integer.