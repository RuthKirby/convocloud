define([
    'jqcloud',
], function(jQCloud) {
    var wordcloud = {};
    var word_array = [];

    wordcloud.setProperties = function() {
    
        $('#wordcloud').jQCloud(word_array, {
            shape: 'rectangular',
            colors: ["#800026", "#bd0026", "#e31a1c", "#fc4e2a", "#fd8d3c", "#3383FF", "#3336FF", "#B233FF"],
            autoResize: true,
            delay: 50,
            fontSize: {
            from: 0.08,
            to: 0.02
                }
        });

    }

    wordcloud.updateCloud = function() {
        $('#wordcloud').jQCloud('update', word_array);
        console.log(word_array);
    }

    wordcloud.updateWordList = function(newWords) {
        word_array.push(newWords)
    }

    wordcloud.clearCloud = function() {
        if (word_array.length > 0) {
            word_array = [];
            $('#wordcloud').jQCloud('update', word_array);
        }
    }

    wordcloud.getLength = function() {
        return word_array.length
    }

    wordcloud.getWords = function() {
        return word_array;
    }

    return wordcloud;
});

    
