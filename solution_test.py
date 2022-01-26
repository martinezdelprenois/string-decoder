import unittest
import re
import solution
class TestDecoder(unittest.TestCase):
    
    def test_regex_matcher(self):
        result = solution.decoder.regex_matcher('43[a]5[cv]')
        self.assertTrue(result, True)
        
    def test_check_string_length(self):
        result = solution.decoder.check_string_length('3[a]2[av]')
        self.assertTrue(result, True)
        
    def test_check_all_integer_values(self):
        result = solution.decoder.check_all_integer_values('301[a]2[av]')
        self.assertFalse(result, False)
        
if __name__ == '__main__':
    unittest.main()

