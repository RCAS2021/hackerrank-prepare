import math
# Which item produced
n = 5

# Probability of defective product
p = 1/3
# Probability of non-defective product
q = 1 - p

b = 0
# Probability of at least 1 being defective in n trials = the probability that the 1st defect is found during the 5 inspections
for i in range(1, n + 1):
    b += math.pow(q, i-1) * p

print(f"{b:.3f}")

#Geometric distribution -> https://www.hackerrank.com/challenges/s10-geometric-distribution-1/tutorial