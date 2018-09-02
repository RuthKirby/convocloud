"""
This is the module responsible for slicing the string into a list
of tokens that can be easily processed. Imports the  3rd party NLTK tokeniser.
Author: Ruth Bovell
Date: 26/08/2017

"""

from nltk.tokenize import regexp_tokenize

def create_tokens (speechstring):
    """
    Using the nltk library it creates 'tokens' from a string
    using expressions to seperate the string by whitespace.
    
    @param speechString: String from stdin
    @return: List of words
    """
    purespeech = regexp_tokenize(speechstring, pattern=r'\w+')
    big_string_only = [word for word in purespeech if len(word) > 1]
    
    return big_string_only
