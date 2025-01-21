from hello import hello


def test_default():
    assert hello()=="Hello, World"

def test_arguments():
    assert hello("Dhyey")=="Hello, Dhyey"

hello("Dhyey")