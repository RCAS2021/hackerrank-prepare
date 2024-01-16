import math
# Number of rejects
x = 2
# Number of trials
n = 10
# Probability of rejects
p = 12/100
# Probability of non-rejects
q = 1 - p

at_least_2 = 0
no_more_2 = 0
# No more than 2 rejects
for i in range(0, x + 1):
    no_more_2 += math.comb(n, i) * math.pow(p, i) * math.pow(q, (n-i))

# At least 2 rejects
for i in range(x, n + 1):
    at_least_2 += math.comb(n, i) * math.pow(p, i) * math.pow(q, (n-i))

print(f"{no_more_2:.3f}")
print(f"{at_least_2:.3f}")

# Binomial distribution I -> Cumulative Probability https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial