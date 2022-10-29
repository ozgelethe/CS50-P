import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    list = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(list)
    
    # counter = {}
    # low = s.lower()
    # if matches := re.search(r"^((/w)? ?)?um([ ]|[.]|[,]|[?]|[!])?(.+)?$", low):
    #     for um in matches:
    #         if um in matches:
    #             counter[um] =0
    #         counter[um] += 1

    # else:
    #     sys.exit



if __name__ == "__main__":
    main()