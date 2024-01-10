

#
# Complete the 'minTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY files
#  2. INTEGER numCores
#  3. INTEGER limit
#

def minTime(files, numCores, limit):
    sum = 0
    files.sort()
    files.reverse()
    for i in range(len(files)):
        if ((files[i] % numCores == 0) and (limit > 0)):
            sum += files[i] // numCores
            limit -= 1
        else:
            sum += files[i]
    print(sum)
        

if __name__ == '__main__':

    files_count = int(input().strip())

    files = []

    for _ in range(files_count):
        files_item = int(input().strip())
        files.append(files_item)

    numCores = int(input().strip())

    limit = int(input().strip())

    result = minTime(files, numCores, limit)
