from sklearn import linear_model
from numpy import multiply

m, n = map(float, input().split())
l_x, l_y = [], []
for i in range(int(n)):
    *elem, y = map(float, input().split())
    l_x.append(elem)
    l_y.append(y)

lm = linear_model.LinearRegression()
lm.fit(l_x, l_y)
a = lm.intercept_
b = lm.coef_

q = int(input())

for i in range(q):
    feat = list(map(float, input().split()))
    print(a + sum(multiply(b, feat)))

# Multiple Linear Regression -> https://www.hackerrank.com/challenges/s10-multiple-linear-regression/tutorial