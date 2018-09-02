"""
This is the main module which starts off the processing of input
from the output of Web Speech API. All the helper modules
needed to process the text are imported here.
Author: Ruth Bovell
Date: 26/08/2017

"""
import json
import sys
import nlp.stemmer as stemmer  # tags the parts of speech and gets root of word
import nlp.tokeniser as tokeniser  # creates a preprocessing friendly list
import nlp.wordremover as wordremover  # removes swears and stop words (the, a, this)
import nlp.importance as importance
from nlp.setupVar import getEnvVariables
getEnvVariables() #gets the location of the NLTK library data

def processText(line):
    """
    Processes text using modules and dumps result to JSON.
    It receives its input from stdin.

    @param String: A speech string from the Web Speech API
    @return: List containing a dictionary of word/value pairs
    """
    #line = sys.stdin.readline()
    tokens = tokeniser.create_tokens(str(line).lower()) #creates a list of the words
    clean_words = wordremover.remove_irreWords(tokens) #removes bad words
    stemmed_words = stemmer.get_stem(clean_words) #gets root of words
    rated_words = importance.rate(stemmed_words) #assigns importance value
    cloud_ready = make_json(rated_words)
    print(str(cloud_ready))
    if (len(cloud_ready) > 0):
        return str(json.dumps(cloud_ready))
    else:
        return {}


def make_json(words):
    """
    Makes the format ready for the Javascript Wordcloud.
    """
    dict_list = [{'text': word, 'weight': score} for word, score in words]
    return dict_list

"""
if __name__ == '__main__':
    processText()

"""

