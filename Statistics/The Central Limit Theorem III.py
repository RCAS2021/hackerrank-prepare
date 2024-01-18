import math
    
n = int(input())
mean = int(input())
std = int(input())
interval = float(input())
z_score = float(input())

# mean' = n * mean
mean_x = n * mean
# std' = sqrt(n) * std
std_x = math.sqrt(n) * std

# A = (mean' - std' * z) / n
A = (mean_x - std_x * z_score) / n
# B = (mean' + std' * z) / n
B = (mean_x + std_x * z_score) / n

print(round(A, 2))
print(round(B, 2))