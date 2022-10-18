def main():

    #get time from user
    answer = input("What time is it? ")

    #call the convert function
    time = convert(answer)

    #define the meal times
    if time >= 7 and time <= 8:
        print("breakfast time")

    if time >= 12 and time <= 13:
        print("lunch time")

    if time >= 18 and time <= 19:
        print("dinner time")

def convert(time):

    # split the time into hour and minutes
    hours, minutes = time.split(":")

    #convert time into float number
    new_minute = float(minutes) / 60

    #return the result to main function
    return float(hours) + new_minute

if __name__ == "__main__":
    main()