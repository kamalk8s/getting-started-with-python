# Defining the function
def get_square(num):
  return num*num

# Executing the function
get_square(100) # It will return 10000
get_square(12) # It will return 144

# Quick Tip: How to write unit tests for your function
def test_square():
  assert get_square(10) == 100
  assert get_square(12) == 144
  assert get_square(11) == 121
# To execute this test. Type: 'pytest -q main.py' in your PowerShell of Terminal.