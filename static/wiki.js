/* The following function is run each time user opens up a language page
in the Flask app.
It fetches links to relevant Wikipedia entries for the given language. */

$(function wiki(){
  var languageAspects = ['phonology', 'grammar', 'dialects'];
  var language = $('#funFactsTitle').text().split(" ")[3];

  for (var i=0; i<languageAspects.length; i++){
    var languageURL =
    'http://en.wikipedia.org/w/api.php?action=opensearch&search=' + language +
    languageAspects[i] + '&format=json&callback=languageCallback';

    $.ajax({
      url: languageURL,
      dataType: "jsonp",
      success: function(response) {
        var entries = response[1];
        language = entries[0];

        if(language == undefined){
          $('#languageResources').append(
            '<li>Wikipedia does not know this language ;)</li>');
        } else {
          var url = 'http://en.wikipedia.org/wiki/' + language;
          $('#languageResources').append('<li><a href="' + url + '">' +
            language + '</a></li>');
        }
      },
      error: function(){
        $('#languageResources').append(
          '<li>Wikipedia is not available ;(</li>');
      }
    });
  }
  return false
});
