$(function wiki(){
  languageAspects = ['phonology', 'grammar', 'dialects']
  language = $('#funFactsTitle').text().split(" ")[3]
  for (var i=0; i<languageAspects.length; i++){
    var languageURL =
    'http://en.wikipedia.org/w/api.php?action=opensearch&search=' + language +
    languageAspects[i] + '&format=json&callback=languageCallback'

    $.ajax({
      url: languageURL,
      dataType: "jsonp",
      success: function(response) {
        var entries = response[1];
        language = entries[0];
        var url = 'http://en.wikipedia.org/wiki/' + language;
        $('#languageResources').append('<li><a href="' + url + '">' + language + '</a></li>');
      }
    });
  }
  return false
});
