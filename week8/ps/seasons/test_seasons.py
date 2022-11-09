from seasons import get_date

def main():
    test_get_date()

def test_get_date():
    assert get_date("1998-05-28") == ("1998", "05", "28")
    assert get_date("1998-5-2") == None
    assert get_date("may 28, 1998") == None

if __name__ == "__main__":
    main()