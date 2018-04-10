from maxima import find_maxima

def test_ez1():
    x = [1, 2, 1, 3, 1, 4]
    ans = [1, 3, 5]
    assert find_maxima(x) == ans

def test_ez2():
    x = [1, 2, 5, 7, 4, 5]
    ans = [3, 5]
    assert find_maxima(x) == ans

def test_sided():
    x = [1, 5]
    ans = [1]
    assert find_maxima(x) == ans

def test_sided2():
    x = [2, 1]
    ans = [0]
    assert find_maxima(x) == ans

def test_nomaxima():
    x = [1, 2, 3, 4, 4]
    ans = []
    assert find_maxima(x) == ans

def test_equalvals():
    x = [1, 2, 2, 1 ,4, 1]
    ans = [4]
    assert find_maxima(x) == ans
