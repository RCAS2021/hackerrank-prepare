import math

mean_a, mean_b = map(float, input().split())
# Calculate X² using poisson distribution's special case
daily_a = 160 + 40 * (mean_a + math.pow(mean_a, 2))
# Calculate Y² using poisson distribution's special case
daily_b = 128 + 40 * (mean_b + math.pow(mean_b, 2))
print(f"{daily_a:.3f}")
print(f"{daily_b:.3f}")

# Possion Distribution (Special Case) -> https://www.hackerrank.com/challenges/s10-poisson-distribution-1/tutorial