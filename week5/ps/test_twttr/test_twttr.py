from twttr import shorten

def main():
    #call test functions
    test_upper_lower()
    test_numbers()
    test_punc()

def test_upper_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TWitteR") == "TWttR"

def test_numbers():
    assert shorten("012345") == "012345"

def test_punc():
    assert shorten("?!'^+%&/()=") == "?!'^+%&/()="

if __name__ == "__main__":
    main()