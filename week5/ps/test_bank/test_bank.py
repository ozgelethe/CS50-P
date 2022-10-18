from bank import value

def main():
    #call test func
    test_return0()
    test_return20()
    test_return100()

#test return 0
def test_return0():
    assert value("hello") == 0
    assert value("hello V") == 0
    assert value("Hello MADAM") == 0

#test return 20
def test_return20():
    assert value("hi") == 20
    assert value("hEY") == 20
    assert value("HEYYYY") == 20

#test return 100
def test_return100():
    assert value("whats up") == 100
    assert value("WELCOME") == 100
    assert value("SWEETYY") == 100

if __name__ == "__main__":
    main()