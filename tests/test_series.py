from math_series import __version__

from math_series.series import fibonacci,fibonacci_list,lucas_list,sum_series_list

def test_version():
    assert __version__ == '0.1.0'


# def test_0():
#     expected=0
#     actual=fibonacci(0)
#     assert expected == actual

# def test_1():
#     expected=1
#     actual=fibonacci(1)
#     assert expected == actual

# def test_2():
#     expected=1
#     actual=fibonacci(2)
#     assert expected == actual

# def test_3():
#     expected=2
#     actual=fibonacci(3)
#     assert expected == actual

# def test_4():
#     expected=3
#     actual=fibonacci(4)
#     assert expected == actual

# def test_5():
#     expected=5
#     actual=fibonacci(5)
#     assert expected == actual

# def test_6():
#     expected=8
#     actual=fibonacci(6)
#     assert expected == actual

# def test_7():
#     expected=13
#     actual=fibonacci(7)
#     assert expected == actual

# def test_fibonacci_list():
#     expected=[0,1,1,2,3,5,8,13,21]
#     actual=fibonacci_list([0,1,2,3,4,5,6,7,8])
#     assert expected == actual

# def test_lucas_list():
#     expected=[2,1,3,4,7,11,18,29,47]
#     actual=lucas_list([0,1,2,3,4,5,6,7,8])
#     assert expected == actual

def test_sum_series_list():
    expected=[2,1,3,4,7,11,18,29,47]
    actual=sum_series_list([0,1,2,3,4,5,6,7,8],2,1)
    assert expected == actual