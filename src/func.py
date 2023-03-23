# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Unit test for the calculate_rectangle_area function
def test_calculate_rectangle_area():
    assert calculate_rectangle_area(3, 4) == 12
    assert calculate_rectangle_area(0, 5) == 0
    assert calculate_rectangle_area(10, 10) == 100

# Function to check if a number is even
def is_even(number):
    return number % 2 == 0
