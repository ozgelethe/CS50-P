import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(time):

    if matches := re.search(r"([0-9][0-2]?):?([0-5][0-9])? (AM|PM) (to) ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)$", time):
        s_hour, s_minute, s_ampm, (to), f_hour, f_minute, f_ampm = matches.groups()

        if int(s_hour) > 12:
            raise ValueError
        if int(f_hour) > 12:
            raise ValueError

        s_time = time24(s_hour, s_minute, s_ampm)
        f_time = time24(f_hour, f_minute, f_ampm)

        return s_time + ' to ' + f_time

    else:
        raise ValueError


def time24(hour, minute, am_pm):

    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    if minute == None:

        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute

    else:
        new_time == f"{new_hour:02}" + ":" + minute

    return new_time

if __name__ == "__main__":
    main()