import math
def cndp(max_, mean_x, std_x):
    # Normal distribution cumulative probability
    return (1 + math.erf((max_ - mean_x) / (std_x * math.sqrt(2)))) / 2

x = int(input())
n = int(input())
mean = float(input())
std = float(input())

# Central Limit Theorem -> N(mean', std')
# mean' = n * mean
mean_x = n * mean
# std' = sqrt(n) * std
std_x = math.sqrt(n) * std

print(round(cndp(x, mean_x, std_x), 4))