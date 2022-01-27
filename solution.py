import re

class StringDecoder:
    """This class decodes an already encoded string"""
        
        
    def regex_matcher(self, encoded_string):
        """Checks that the encoded string matches the regex pattern

        Parameters
        ----------
        encoded_string : str
            The encoded string whose pattern has to match the pattern
        """

        pattern = '(\d{1,}\[[a-z]{1,}\])+'
        result = re.match(pattern,encoded_string)
        
        if result:
            return True
        else:
            return False
        
    def check_string_length(self, encoded_string):
        """Checks that the encoded string length is 30

        Parameters
        ----------
        encoded_string : str
            The encoded string whose length is checked
        """
        if (len(encoded_string) <= 30 and len(encoded_string) >= 1):
            return True
        else:
            return False
        
    def check_all_integer_values(self, encoded_string):
        """Checks that the encoded string numbers are in the range of [1,300]

        Parameters
        ----------
        encoded_string : str
            The encoded string whose numbers are to be checked
        """
        
        number_item = 0
        string_result = ''
        stack = []
        numbers = []
        
        for item in encoded_string:
            if item.isdigit():
                number_item = number_item * 10 + int(item)
                numbers.append(number_item)
                
            elif item.isalpha():
                    string_result += item
                    
            elif item == '[':
                    
                stack.append((string_result, number_item))
                string_result, number_item = '', 0
        if all(element < 300 and element > 0 for element in numbers):
            return True
        else:
            return False
                
    def string_decode(self, encoded_string):
        """Decodes the encoded string

        Parameters
        ----------
        encoded_string : str
            The encoded string to be decoded
        """
        
        if (self.check_string_length(encoded_string) and self.check_all_integer_values(encoded_string)) and (self.regex_matcher(encoded_string)):
        
            stack = []
            result = ''
            number = 0
            for element in encoded_string:
                if element.isdigit():
                    number = number * 10 + int(element)
                    
                elif element.isalpha():
                    result += element
                    
                elif element == '[':
                    
                    stack.append((result, number))
                    
                    result, number = '', 0 # resetting the result and number
                                    
                    
                else:
                    last_str, this_num = stack.pop()
                    result = last_str + this_num * result # open the bracket and repeat the character by the number
            print(result)
            return result
        
decoder = StringDecoder()
decoder.string_decode('10[a]5[cv]') # example

    
    
    