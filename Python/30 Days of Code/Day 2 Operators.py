#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def calcPercentage(initial_cost, percent):
    return initial_cost * (percent / 100)

def solve(meal_cost, tip_percent, tax_percent):
    print(round(meal_cost + calcPercentage(meal_cost, tip_percent) + calcPercentage(meal_cost, tax_percent)))


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)