import math
# Number of sucesses
x = 3
# Number of trials
n = 6
# Ratio Boys:Girls
ratio = list(map(float, input().split()))
# Probability of boys or probability of success
p = ratio[0] / (sum(ratio))
# Probability of girls or probability of failure
q = 1 - p
b = 0
# Sum start = i = x, end = n included
for i in range(x, n + 1):
    # Sum Binomial Distribution where x = i, n, p => b(x = i, n, p)
    b += math.comb(n, i) * math.pow(p, i) * math.pow(q, (n-i))
print(f"{b:.3f}")

#binomial distribution I -> Cumulative Probability https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial