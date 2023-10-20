#Using example
#1
#7
#1 5 4 3 2 6 8
def findZigZagSequence(a, n):
    a.sort()
    mid = int(((n)/2))-1 #Change 1 (...-1) #middle_num = 3 (3.5-1)

    a[mid], a[n-1] = a[n-1], a[mid] #a[mid] -> middle num /// a[n-1] -> last num /// swap them -> 1 2 3 4 5 6 8 -> 1 2 3 8 5 6 4
    st = mid + 1 #st = middle num +1 (5)
    ed = n - 2 #Change 2 (n-1 -> n-2) #ed = second-last num (6)
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st] #a[st] -> middle num +1 /// a[ed] -> second last num /// swap them -> 1 2 3 8 5 6 4 -> 1 2 3 8 6 5 4
        st = st + 1 #Moves to middle num + 2
        ed = ed - 1 #Change 3 (+1 -> -1) #Moves to third last num

    for i in range (n): #Prints the array
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)