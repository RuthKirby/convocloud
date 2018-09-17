# ConvoCloud

ConvoCloud is an app that provides a real-time visualisation of the semantic content of spoken language. It achieves this by integrating the technologies of Automatic Speech Recognition, Natural Language Processing and Word Cloud generation.

# Compatability & Demo

This first version currently runs in Google Chrome Desktop. An alpha demo can be tried out [here](http://convocloud.dapper17.com).

# Use Cases

With fixes and additions it could possibly be used by those with hearing impairments as an assistive tool for capturing the topics of a spoken conversation. Other possible use cases include lectures, meetings and other scenarios where a semantic summary of what is being said would be useful. 

# Screenshot

![ConvoCloud Example][example]

[example]: https://cdn.rawgit.com/RuthKirby/convocloud/34a92704/example_pics/example_1.PNG "ConvoCloud Example"

# Importance Algorithm

The importance, i.e. size, of a word in the cloud is currently determined by a) frequency b) syntactic word class c) character length. However, this is still being adjusted. 

# Tech/FrameWorks Used

## Web

This is a Flask web app that utlises [Flask-Bootstrap](https://github.com/mbr/flask-bootstrap). RequireJS is responsible for serving the JavaScript modules. To send speech input to the web server for processing the app uses SocketIO. 

## Automatic Speech Recognition

To capture speech input for the cloud the [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) is used.

## Natural Language Processing

The python scripts that process the raw speech input and create semantically useful tokens for visualisation make use of the [Natural Language Toolkit](https://www.nltk.org/). This includes: tokenisation, removal of stop words and swear words and lemmatisation.

## Word Cloud Generation

The bright and beautiful word clouds are rendered using the [JQcloud](http://mistic100.github.io/jQCloud/) library. 