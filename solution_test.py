import unittest
import re
import solution
class TestDecoder(unittest.TestCase):
    
    def test_string_decoder(self):
        pass
    
    def test_regex_matcher(self):
    
        result = solution.decoder.regex_matcher('klfdjlkjdsfkj3j4rlkj3fjdlf')
        self.assertTrue(result, True)
        
if __name__ == '__main__':
    unittest.main()

