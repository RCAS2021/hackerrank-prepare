import math
# lambda -> average number of successes
mean = 2.5
# k -> actual number of successes or random variable
x = 5
print(f"{(math.pow(mean, x) * math.pow(math.e, -mean))/math.factorial(x):.3f}")

#Poisson Distribution -> https://www.hackerrank.com/challenges/s10-poisson-distribution-1/tutorial