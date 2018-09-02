$(document).ready(function() {

    define([
         'wordcloud', 'speechtotext'
    ], function(wordcloud, speechtt) {

        wordcloud.setProperties();
        speechtt.listen();

        $('#startbutton').on('click', (function() {
            speechtt.dictate();
            $('#alertBoxOn').show(); 
            $('#alertBoxOff').hide();
            $('#alertBoxClear').hide();
        }));
    
        $('#stopbutton').on('click', (function() {
            speechtt.stopDictate();
            $('#alertBoxOff').show();
            $('#alertBoxOn').hide();
            $('#alertBoxClear').hide();
        }));

        $('#clearbutton').on('click', (function() {
            $('#alertBoxOff').hide();
            $('#alertBoxOn').hide();
            $('#alertBoxClear').show();
        }));

        $('#clearbutton').on('click', (function() {
            wordcloud.clearCloud();
        }));
        
    });

});