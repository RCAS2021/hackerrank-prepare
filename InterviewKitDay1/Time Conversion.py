def timeConversion(s):
    format = s.split(":")
    if("PM" in format[2]):
        format[2] = format[2].strip("PM")
        hour = int(format[0])
        if(hour == 12):
            hour = 12
        else:
            hour += 12
            format[0] = str(hour)
        format = ":".join(format)
        print(format)
    else:
        format[2] = format[2].strip("AM")
        hour = int(format[0])
        if(hour == 12):
            format[0] = "00"
        format = ":".join(format)
        print(format)
    
if __name__ == '__main__':
    s = input()

    result = timeConversion(s)