import re

class Decoder:
    def string_decode(self, encoded_string):
        
        print(encoded_string)
        
    def regex_matcher(self, encoded_string):
        pattern = 'super'
        result = re.match(pattern,encoded_string)
        
        if result:
            return True
        else:
            return False
        
decoder = Decoder()
decoder.string_decode('3[a]2[bc]')
decoder.regex_matcher('superstition')
    
    
    