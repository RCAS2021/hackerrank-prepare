import math
# Which item produced
n = 5
# Probability of defective product
p = 1/3
# Probability of non-defective product
q = 1 - p
# Geometric distribution formula
g = math.pow(q, (n-1)) * p

print(f"{g:.3f}")

#Geometric distribution -> https://www.hackerrank.com/challenges/s10-geometric-distribution-1/tutorial