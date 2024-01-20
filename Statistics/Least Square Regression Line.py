import statistics as st

x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

mean_x = st.mean(x)
mean_y = st.mean(y)

std_x = st.pstdev(x)
std_y = st.pstdev(y)

# Calculating pearson coefficient
sum_ = 0
for i in range(len(x)):
    sum_ += ((x[i] - mean_x) * (y[i] - mean_y))

p = sum_ / (len(x) * std_x * std_y)

# Calculating Regression Line
b = p * (std_y / std_x)
a = mean_y - b * mean_x

print(round(a + b * 80, 3))

# Pearson Correlation Coefficient -> https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/tutorial
# regression line -> https://www.hackerrank.com/challenges/s10-least-square-regression-line/tutorial