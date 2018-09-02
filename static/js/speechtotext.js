define([
    'socket', 'wordcloud'
], function(io, wordcloud) {

    var speechtt = {};
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.continuous = true;
    var final_transcript = '';
    var transcript = '';
    var isSpeechRecOn = false;

    speechtt.listen = function() {
        socket.on('connect', function() {
            // we emit a connected message to let knwo the client that we are connected.
                $('#connection').append('<p>Connection: Successful!</p>');
            });
        
        socket.on('processed', function(msg) {
            
            if (msg.length > 0) {
                var stringy = msg;
                console.log(stringy);

                var newWords = JSON.parse(msg)
                var currentWords = wordcloud.getWords();
                var nwLength = newWords.length;
                var cwLength = wordcloud.getLength();
                var duplicate = false;
                for (var i = 0; i < nwLength; i++) {
                    for (var f = 0; f < cwLength; f++) {
                        if (newWords[i].text == currentWords[f].text) {
                            currentWords[f].weight++;
                            duplicate = true;
                        }
                    }
                    if (duplicate == false) {
                        wordcloud.updateWordList(newWords[i]);
                    }
                    
                }
                
                wordcloud.updateCloud();
            }
            
        });
        
    }

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

    speechtt.stopDictate = function() {
        recognition.stop();
        isSpeechRecOn = false;
    }

    return speechtt;
    
});