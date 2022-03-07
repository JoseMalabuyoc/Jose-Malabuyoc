import unittest
from unittest.mock import Mock
import csvparser

class TestParser(unittest.TestCase):
    def test_read_row(self):
        file = Mock()
        # Setup/Configuration
        file.configure_mock(**{'readline.return_value':'\'Vehicle1\',\'Vehicle2\''})
        # Expected output
        expected = ("'Vehicle1' - 'Vehicle2'")
        result = csvparser.read_row(file)
        print(result)
        # Assertion
        assert result == expected
    
if __name__ == "__main__":
    unittest.main()
