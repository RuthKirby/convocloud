"""
This module calculates the importance of a word using its 
linguistic word class and character length.
Author: Ruth Bovell
Date: 21/08/2018
"""

def rate (words):
    crted = class_rate(words)
    lngthrtd = length_rate(crted)
    return lngthrtd


def class_rate (words):
    """
    Rates list of word/wordclass tuples
    """
    class_rated = []
    for word, wordclass in words:
    
        if wordclass in ('n', 'v'):

            class_rated.append([word, 3])
        
        elif wordclass in ('a'):
            class_rated.append([word, 2])

        else:
            class_rated.append([word, 1])

    return class_rated

def length_rate (words):
    """
    Rates a list of word/score tuples that have already been class rated.
    """
    length_rated = [[word, score + 3] if len(word) > 9 else [word, score + 2] if len(word) > 5 else [word, score + 1] for word, score in words]

    return length_rated