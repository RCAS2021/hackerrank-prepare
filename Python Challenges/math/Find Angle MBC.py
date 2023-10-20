import math

lengthAB = int(input())
lengthBC = int(input())

angle = round(math.degrees(math.atan2(lengthAB, lengthBC)))
print(f"{angle}{chr (176)}")