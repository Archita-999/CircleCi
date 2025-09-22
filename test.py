# Import the unittest module
import unittest  

# Import the function to_upper from the main.py file
from main import to_upper

# Create a test case class that inherits from unittest.TestCase
class MyTestCase(unittest.TestCase):

    # Define a test method to check if to_upper() works correctly
    def test_to_upper(self):
        name = "Archita"                      # Input string
        upper_name = to_upper(name)           # Call the function
        self.assertEqual(upper_name, "ARCHITA")  # Expected output in uppercase

# This block runs the tests when the file is executed directly
if __name__ == '__main__':
    unittest.main()
