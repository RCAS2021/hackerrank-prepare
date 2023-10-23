def dayOfProgrammer(year):
    day = 13
    if (year == 1918):
        day = 26
    if (year > 1917):
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            day = 12
    else:
        if (year % 4 == 0):
            day = 12
            
    print(f"{day}.09.{year}")
if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)