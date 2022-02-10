import pytest
from Teil_4_Testing.tutorial import my_functions


def test_multiply_by_2_happypath():  # test for correct execution (different values)
    assert my_functions.multiply_by_2(0) == 0
    assert my_functions.multiply_by_2(1) == 2
    assert my_functions.multiply_by_2(2) == 4
    assert my_functions.multiply_by_2(3) == 6

@pytest.mark.parametrize('input,expected', [  # schreibe die Variablennamen in Anführungszeichen
    (-1, -2),
    (-3, -6),
    (4, 8),
    (5, 10)
])
def test_multiply_by_2_parametrized_happypath(input, expected):  # test for correct execution (different values)
    assert my_functions.multiply_by_2(input) == expected, "test failed because " + str(input) + "*2/=" + str(expected)

# Error Handling
def test_multiply_by_2_extremepath(): #test for correct execution (error)
    with pytest.raises(ZeroDivisionError): #erwartet, dass ein ZeroDivisionError geworfen wird; passiert das nicht wird ein Fehler geworfen
        1 / my_functions.multiply_by_2(0)

def test_absolute_value_happypath_positive():  # test for correct excecution (positive values)
    assert my_functions.absolute_value(0) == 0
    assert my_functions.absolute_value(1) == 1
    assert my_functions.absolute_value(2) == 2
    assert my_functions.absolute_value(3) == 3

def test_absolute_value_happypath_negative():  # test correct excecution (negative values)
    assert my_functions.absolute_value(0) == 0
    assert my_functions.absolute_value(-1) == 1
    assert my_functions.absolute_value(2) == 2
    assert my_functions.absolute_value(-3) == 3