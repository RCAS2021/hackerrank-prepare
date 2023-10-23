def bonAppetit(bill, k, b):
    anna = (sum(bill) - bill[k])//2
    if(b - anna == 0):
        print("Bon Appetit")
    else:
        print(b - anna)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
