#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):

    for i in range(len(grid)):
        grid[i]=sorted(grid[i])

    for j in range(len(grid[0])):
        for i in range(1, len(grid)):
            if (grid[i-1][j])>(grid[i][j]):
                return "NO"

    return "YES"

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)
