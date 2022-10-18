#create list with the name of all months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#loop forever
while True:
    #get a date from user, hope it'll work :d
    date = input("Date: ").strip()

    try:
        #split date by /
        month, day, year = date.split("/")

        #check if month is in between 1 and 12, and day between 1 and 31 ehehehhr
        if ( int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            #split the date by space
            old_month, old_day, year = date.split(" ")

            #find the number of the month
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1

            #remove comma from day variable
            day = old_day.replace(",", "")
            if not old_day.endswith(","):
                continue

            #check if month is in between of 1 and 12 and day between 1 and 31
            if ( int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            #go to the next line
            print()
            pass

#if month is less than 10, add a 0 before
#if day is less than 10, add a 0 before
#print the result
print(f"{year}-{int(month):02}-{int(day):02}")

