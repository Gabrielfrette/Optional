import math
import pytest
from calculator import add, factorial, sin, divide, multi, minus


def test_add_exercise_1():
    assert add(1, 2) == 3

def test_float_exercise_2():
    return math.isclose(add(0.1,0.2), 0.3)

def test_string_exercise_3():
    assert add("Hello ", "World") == "Hello World"

def test_factorial_exercise_4a():
    assert factorial(5) == math.factorial(5)

def test_sin_exercise_4b():
    assert abs(sin(1,2000) - math.sin(1))< 1e-12

def test_divide_exercise_4c():
    assert divide(10,2) == 5

def test_multi_exercise_4d():
    assert multi(3,4) == 12

def test_minus_exercise_4d():
    assert minus(5,2) == -3


import pytest 

def test_add_error_exercise_5():
    with pytest.raises(TypeError):
        add(1,"Hei")

def test_divide_zero_exercise_5():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)

# Exercise 6
@pytest.mark.parametrize("arg, expected_output", [[(-1, -3), -4], [(1,5), 6], [(5,3), 8]])
def test_add(arg, expected_output):
    assert add(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(0.1, 0.1), 0.2], [(0.1,0.2), 0.3], [(0.2,0.2), 0.4]])
def test_float(arg, expected_output):
    x = add(float(arg[0]), float(arg[1]))
    assert abs(x - expected_output) < 1e-12


@pytest.mark.parametrize("arg, expected_output", [[("Hello ", "World"), "Hello World"], [("Hi ", "There"), "Hi There"], [("Ja ", "Vi"), "Ja Vi"]])
def test_string(arg, expected_output):
    assert add(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[5, math.factorial(5)], [4, math.factorial(4)], [3, math.factorial(3)]])
def test_factorial(arg, expected_output):
    assert factorial(arg) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(1, 1000), math.sin(1)], [(10, 500), math.sin(10)], [(20, 1000), math.sin(20)]])
def test_sin(arg, expected_output):
    assert abs(sin(arg[0], arg[1]) - expected_output) < 1e-6

@pytest.mark.parametrize("arg, expected_output", [[(10, 2), 5], [(100, 4), 25], [(45, 5), 9]])
def test_divide(arg, expected_output):
    assert divide(arg[0],arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(10, 2), 20], [(100, 4), 400], [(45, 5), 225]])
def test_multi(arg, expected_output):
    assert multi(arg[0],arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(10, 4), 6], [(50, 25), 25], [(40, 29), 11]])
def test_minus(arg, expected_output):
    assert minus(arg[1],arg[0]) == expected_output


