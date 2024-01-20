import statistics as st
#import math

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

mean_x = st.mean(x)
mean_y = st.mean(y)
#std_x = math.sqrt(sum((i - mean_x)**2 for i in x) / len(x))
#std_y = math.sqrt(sum((i - mean_y)**2 for i in y) / len(y))
std_x = st.pstdev(x)
std_y = st.pstdev(y)

sum_ = 0
for i in range(n):
    sum_ += ((x[i] - mean_x) * (y[i] - mean_y))
print(sum_ / (n * std_x * std_y))

# Pearson Correlation Coefficient -> https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/tutorial