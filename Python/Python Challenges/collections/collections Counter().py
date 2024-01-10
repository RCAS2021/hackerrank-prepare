from collections import Counter
buy = []
sumB = 0

X = int(input())
sizes = list(map(int, input().split()))
N = int(input())

count = Counter(sizes)
for i in range(N):
    customer, price = map(int, input().split())
    buy.append([customer, price])

for i in buy:
    if(count[i[0]] > 0):
        sumB += i[1]
        count[i[0]] -= 1
print(sumB)

#count.update({buy[i][0]: count[i]-1}) #Updates the value in the given key
#count.pop(buy[i][0]) #Removes the value in the given key