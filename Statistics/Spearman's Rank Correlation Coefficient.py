n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

s_x = sorted(x)
s_y = sorted(y)

r_x = []
r_y = []

sum_ = 0
for i in range(n):
    for j in range(n):
        if (x[i] == s_x[j]):
            r_x.append(j + 1)
        if (y[i] == s_y[j]):
            r_y.append(j + 1)
    
for i in range(n):
    sum_ += (r_x[i] - r_y[i]) ** 2
r_xy = 1 - ((6 * sum_) / (n * (n ** 2 - 1)))

print(round(r_xy, 3))

# Spearman Rank Correlation Coefficient -> https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/tutorial