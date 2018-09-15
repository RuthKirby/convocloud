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
    unique = True
    print(str(words))
    for word, wordclass in words:

        if len(class_rated) > 0:
            """
            for seenword, score in class_rated: 
                if word == seenword:
                    score = score + 1
                    print(str(score))
                    unique = False
            """
            for x in class_rated: #Increment score of word if duplicate
                if x[0] == word:
                    x[1] = x[1] + 1
                    unique = False

            #class_rated = [[seenword, score + 1] unique = false if word == seenword else [seenword, score] for seenword, score in class_rated]

        if unique: #Only add to the list of words if it is a new word
            if wordclass in ('n', 'v'):

                class_rated.append([word, 3])
            
            elif wordclass in ('a'):
                class_rated.append([word, 2])

            else:
                class_rated.append([word, 1])
        
        unique = True

    return class_rated

def length_rate (words):
    """
    Rates a list of word/score tuples that have already been class rated.
    """
    length_rated = [[word, score + 3] if len(word) > 9 else [word, score + 2] if len(word) > 5 else [word, score + 1] for word, score in words]

    return length_rated