define([
    'socket', 'wordcloud'
], function(io, wordcloud) {
    /**
     * speechtts module - Defines functions that manipulate the result from the Web Speech API and event listeners
     * for communication with the Flask server.
     * @exports socket
     * @exports wordcloud
     */

    var speechtt = {};
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.continuous = true;
    var final_transcript = '';
    var transcript = '';
    var isSpeechRecOn = false;

    /**
     * Listeners for when the server connects and when it sends back words 
     * that have been through natural language processing.
     */
    speechtt.listen = function() {
        socket.on('connect', function() {
                $('#connection').append('<p>Connection: Successful!</p>');
            });
        
        socket.on('processed', function(msg) {
            
            if (msg.length > 0) {
                var stringy = msg;
                console.log(stringy); //string of the returned words

                var newWords = JSON.parse(msg)
                var currentWords = wordcloud.getWords();
                var nwLength = newWords.length;
                var cwLength = wordcloud.getLength();
                var duplicate = false;
                for (var i = 0; i < nwLength; i++) { // for every new word the current word set is searched
                    for (var f = 0; f < cwLength; f++) {
                        if (newWords[i].text == currentWords[f].text) { //if new word is already present increment weight
                            console.log(newWords[i].text + "has been said before!")
                            currentWords[f].weight++;
                            duplicate = true;
                        }
                    }

                    if (duplicate == false) { //if new word is not present then add to word set
                        console.log(newWords[i].text + "is a new word!")
                        wordcloud.updateWordList(newWords[i]);
                    }

                    duplicate == false;
                    
                }
                
                wordcloud.updateCloud();
            }
            
        });
        
    }

    /**
     * Listeners for Web Speech API event: 
     * (onresult) - if speech is detected send to Python server
     * (onend) - show alert box that says speech recognition has stopped
     * (onaudiostart) - show alert box that says speech recognition is active
     */
    speechtt.dictate = function() {
        if (isSpeechRecOn == false) {
            recognition.start();
            isSpeechRecOn = true;
        }
        
        recognition.onresult = (event) => {
            for (var i = event.resultIndex; i < event.results.length; ++i) {
                
                final_transcript += event.results[i][0].transcript;

                transcript = event.results[i][0].transcript;
                socket.emit('json_button', transcript);
                //console.log(transcript);
                
            }
            
        }

        recognition.onend = (event) => {
            isSpeechRecOn = false;
            $('#alertBoxOn').hide();
            $('#alertBoxOff').show();
        }

        recognition.onaudiostart = (event) => {
            $('#alertBoxOn').show();
            $('#alertBoxOff').hide();
        }
       
    }

    /**
     * Stops speech recognition
     */
    speechtt.stopDictate = function() {
        recognition.stop();
        isSpeechRecOn = false;
    }

    return speechtt;
    
});