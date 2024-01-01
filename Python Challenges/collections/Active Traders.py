#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#
from collections import Counter
def mostActive(customers, customers_count):
    total = Counter(customers)
    companies = []
    for i in total:
        if (total[i] / customers_count >= 5/100):
            companies.append(i)
    companies.sort()
    print(*companies, sep="\n")
    
if __name__ == '__main__':

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers, customers_count)