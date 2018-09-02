"""
This is the module responsible for tagging parts of speech and
stripping words of their morphology. It imports the 3rd party POS
Ripple Tagger.
Author: Ruth Bovell
Date: 26/08/2017

"""
import os
import nltk
from rippletagger.tagger import Tagger
from nltk.stem import WordNetLemmatizer

def get_tag(tag):
    """
    Converts NLTK tags into tags the Wordnet lemmatizer can understand.

    @param tag: NLTK tag as a string
    @return: Wordnet tag as a string
    """
    if tag.startswith(('NO')):
        return 'n'
 
    if tag.startswith(('V', 'AU')):
        return 'v'
 
    if tag.startswith('AD'):
        return 'a'
 
    if tag.startswith('R'):
        return 'r'
 
    return 'OTHER'

def get_stem(tokens):
    """
    Gets the root of words by tagging them syntactically
    and then using WordNet lemmatizer.

    @param tokens: list containing morphologically rich words
    @return: A list of words stripped to their root 
    """
    
    tagger = Tagger(language="en") #creates Ripple Tagger
    tagged = tagger.tag(tokens) #creates list of tokens with tags
    lemmat = WordNetLemmatizer() #creates instance of lemmatizer
    stemmed = []
    for token,tag in tagged:
    
        wordnettag = get_tag(tag)
        if (get_tag(tag) == 'OTHER'): #words with unknown tags are added as they are
            stemmed.append([token, tag])
        else:
            stem = lemmat.lemmatize(token, wordnettag)
            stemmed.append([stem, wordnettag])

    return stemmed

#if __name__ == "__main__":
    #getStem()