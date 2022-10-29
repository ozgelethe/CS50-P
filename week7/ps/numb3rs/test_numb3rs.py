from numb3rs import validate

def main():
    test_number_of_byte()
    test_numbers()

def test_number_of_byte():
    assert validate(r"45.62.52.13.15") == False
    assert validate(r"12.0.1") == False
    assert validate(r"45.31") == False
    assert validate(r"1") == False
    assert validate(r"15.24.62.15") == True

def test_numbers():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.512.512.512") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"cat") == False
    assert validate(r"12.300.400.500") == False


