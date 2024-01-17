import math
# mean
mean = 20
# standard deviation
std = 2

# values less than or equal
x = 19.5
y1 = 20
y2 = 22

# Cumulative probabilities
p_x = 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))
p_y1 = 0.5 * (1 + math.erf((y1 - mean) / (std * math.sqrt(2))))
p_y2 = 0.5 * (1 + math.erf((y2 - mean) / (std * math.sqrt(2))))

# Chance between y1 and y2
p_y = p_y2 - p_y1
    
print(round(p_x, 3))
print(round(p_y, 3))

#Normal Distribution (Cumulative Probability) -> https://www.hackerrank.com/challenges/s10-normal-distribution-1/tutorial