import math
mean = 70
std = 10

# Lower than or equal to 80 
y = 80
# Lower than or equal to 60
z = 60

# Percentage probability of lower than or equal to 60
p_60 = 0.5 * (1 + math.erf((z - mean) / (std * math.sqrt(2)))) * 100
# Percentage probability of lower than or equal to 60
p_80 = 0.5 * (1 + math.erf((y - mean) / (std * math.sqrt(2)))) * 100

# Probability of more than 60 = 100(percentage) - probability of 60
p_more_60 = 100 - p_60

# Probability of more than 80 = 100(percentage) - probability of 80
p_more_80 = 100 - p_80


print(f"{p_60:.2f}")
print(f"{p_more_60:.2f}")
print(f"{p_more_80:.2f}")

#Normal Distribution (Cumulative Probability) -> https://www.hackerrank.com/challenges/s10-normal-distribution-1/tutorial