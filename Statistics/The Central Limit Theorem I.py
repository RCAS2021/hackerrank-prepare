import math
def cndp(max_, mean_x, std_x):
    # Normal distribution cumulative probability
    return (1 + math.erf((max_ - mean_x) / (std_x * math.sqrt(2)))) / 2

max_ = int(input())
load = int(input())
mean = int(input())
std = int(input())

# Central Limit Theorem -> N(mean', std')
# mean' = n * mean
mean_x = load * mean
# std' = sqrt(n) * std
std_x = math.sqrt(load) * std

print(round(cndp(max_, mean_x, std_x), 4))