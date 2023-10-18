def timeConversion(s):
    format = s.split(":")
    if("PM" in format[2]):
        hour = int(format[0])
        if(hour == 12):
            hour = 12
        else:
            hour += 12
            format[0] = hour
        format[2] = format[2].strip("PM")
        print(f"{format[0]}:{format[1]}:{format[2]}")
    else:
        format[2] = format[2].strip("AM")
        hour = int(format[0])
        if(hour == 12):
            format[0] = "00"
        print(f"{format[0]}:{format[1]}:{format[2]}")
    
if __name__ == '__main__':
    s = input()

    result = timeConversion(s)