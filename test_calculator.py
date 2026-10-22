from calculator import Calculator

def test_add():
    # Arrange
    calc = Calculator()
    # Act
    result = calc.add(2, 3)
    # Assert
    assert result == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
