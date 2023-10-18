import numpy as np

N, M = np.array(input().split(), dtype=int)

for i in range(1, N, 2): #Starts i = 1, ends i = N, step = 2. EX: (7 21) -> starts i = 1, ends i = 7, step = 2.
    print((".|."*i).center(M, '-')) #Prints the pattern *i(number of times = i) then centers(width=M, fill_with='-') 
    #EX: (7 21) -> prints(".|."*1) then centers. 
    # Next for loop -> (i = 3) prints(".|."*3) then centers. 
    # Next for loop -> (i = 5) prints(".|."*5) then centers. 
    # Next for loop -> (i = 7) prints(".|."*7) then centers.

print(("WELCOME").center(M, '-')) #Prints welcome then centers.

for i in range(N-2, -1, -2): #Starts i = N-2, ends i = -1, step -2. EX (7 21) -> starts i = 5, ends i = -1, step = -2.
    print((".|."*i).center(M, '-')) #Prints the pattern *i(number of times = i) then centers(width=M, fill_with='-') 
    #EX:(7 21) -> prints(".|."*5) then centers. 
    # Next for loop -> (i = 3) prints(".|."*3) then centers.
    # Next for loop -> (i = 1) prints(".|."*1) then centers.
    # Next for loop -> (i = -1) prints(".|."*-1)(does not print) then centers.
