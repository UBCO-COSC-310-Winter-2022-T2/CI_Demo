from src.func import *

# Unit test for the is_even function
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    
# Unit test for the calculate_rectangle_area function
def test_calculate_rectangle_area():
    assert calculate_rectangle_area(3, 4) == 12
    assert calculate_rectangle_area(0, 5) == 0
    assert calculate_rectangle_area(10, 10) == 100

def test_calculate_square_area():
    assert calculate_square_area(5)  == 25
    assert calculate_square_area(0)  == 0
    assert calculate_square_area(10)  == 100

def test_calculate_circle_area():
    assert calculate_circle_area(0)   == 0
    assert calculate_circle_area(1)   == 3.14