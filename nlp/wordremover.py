"""
This is the module responsible for removing stop words (list of
stop words are gathered from the NLTK corpus). It also removes curse
words that are listed on the site 'www.bannedwordlist.com'.
Author: Ruth Bovell
Date: 21/08/2017

"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, regexp_tokenize
import os
import sys

def create_swear_list():
    """
    Creates a list of banned words from an adapted file downloaded
    from www.bannedwordlist.com. It then makes them into a list containing only those
    that have more than 1 character.

    @return: List of swear word strings from .txt file
    """
    #bannedWords = open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "resource/swearWords.txt"), mode='r')
    bannedWords = open("nlp/resource/swearWords.txt")
    contents = bannedWords.read()
    swears = word_tokenize(contents)
    #Only have a list of swear words longer than 1 character
    swears = [word for word in swears if len(word) > 1]
    bannedWords.close()
    return swears
    

def remove_irreWords(tokens):
    """
    Adds stop words to a list of words to remove. It also adds swear
    words to that same list and cleans the inputted token list.

    @param tokens: List of unfiltered string tokens
    @return: List of filtered token strings
    """
    wordsToDelete = stopwords.words('english')
    wordsToDelete.extend(create_swear_list())
    cleanTokens = [word for word in tokens if word not in wordsToDelete]
    return cleanTokens
