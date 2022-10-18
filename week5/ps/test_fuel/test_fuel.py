from fuel import convert, gauge
import pytest

def main():
    test_zero()
    test_convert()
    test_gauge()

#in order to write assertions about raised exeptions, you can use pytest.raises()
#as a context manager like this:

# import pytest
# def test_zero_division():
    # with pytest.raises(ZeroDivisionError):
        # 1 / 0

#test ZeroDivisionError
def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

#test ValueError
def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")

#test correct input
def test_convert():
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("2/3") == 67

def test_gauge():
    assert gauge(25) =="25%"
    assert gauge(1) =="E"
    assert gauge(99) =="F"
    assert gauge(10) =="10%"


if __name__ == "__main__":
    main()