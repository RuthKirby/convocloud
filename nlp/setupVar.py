"""
Sets up the enviroment variables: currently the location
of the data needed by the NLTK library.
"""
import os

def getEnvVariables():
    os.environ['NLTK_DATA'] = os.path.join(os.path.dirname(__file__),'nltk_data')