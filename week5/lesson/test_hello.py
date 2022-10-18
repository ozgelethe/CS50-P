from python.week5.lesson.hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("rukis") == "hello, rukis"