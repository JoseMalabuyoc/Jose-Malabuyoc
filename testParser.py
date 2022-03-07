import unittest
from unittest.mock import Mock, patch
import csvparser

# unittest for parse_row

class testParser(unittest.TestCase):
    def test_parse_row(self):
        #test = str and int with symbol
        test = "Ford,Nissan,Toyota,90%\n"
        expected = "Ford - Nissan - Toyota - 90%"
        print(expected)
        result = csvparser.parse_row(test)
        print(result)
        self.assertEqual(result, expected)
        
# unittest for read_row

class testRead(unittest.TestCase):

    @patch("csvparser.parse_row")
    def test_read_row(self, mock_parse_row):
    #test = len(next_line) > 0 to rtn str
        file = Mock()
        file.configure_mock(**{'readline.return_value': "Ford,Nissan,Toyota,90%\n"})
        mock_parse_row.return_value = "Ford - Nissan - Toyota - 90%\n"
    
        result = csvparser.read_row(file)
        expected = mock_parse_row.return_value
        self.assertEqual(result, expected)