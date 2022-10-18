from plates import is_valid

def main():
    test_size()
    test_first2()
    test_numbers()
    test_zero()
    test_punc()

#check the size
def test_size():
    assert is_valid("AAA222") == True
    assert is_valid("CS50") == True
    assert is_valid("S") == False
    assert is_valid("SS") == True

#check first 2 letter
def test_first2():
    assert is_valid("50CS") == False
    assert is_valid("SA54") == True
    assert is_valid("54AVD") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False

#check if there are numbers in middle
def test_numbers():
    assert is_valid("CCC333") == True
    assert is_valid("RUK1S") == False

#check zeros
def test_zero():
    assert is_valid("CC0633") == False
    assert is_valid("RUK01S") == False
    assert is_valid("CSP501") == True

#check punc
def test_punc():
    assert is_valid("CC 3.3") == False
    assert is_valid("RUK!S") == False
    assert is_valid("CSX30") == True

if __name__ == "__main__":
    main()