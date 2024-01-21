n = int(input())

phonebook = {}
for i in range(n):
    values = input()
    name = values.split()[0]
    number = values.split()[1]
    
    phonebook[name] = number
    
queries = input()

while queries:
    if queries in phonebook:
        print(queries+"="+phonebook.get(queries))
    else:
        print("Not found")
    
    try:
        queries = input()
    except EOFError:
        break