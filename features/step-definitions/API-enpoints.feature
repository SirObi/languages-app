Feature -> API endpoints

As a programmer
I would like to be able to access publicly available data on the website programmatically
So that I can use the data in my app, regardless of the language I’m using

Scenario: GET request for list of language families
Given the language families table is not empty
When I send a request for list of language families
Then I receive a JSON with list of families

Scenario: GET request for language family
Given the language family exists
When I send a request for language family
Then I receive a JSON with requested language family
  And the JSON contains list of languages in family

Scenario: GET request for language
Given the language exists
When I send a request for language
Then I receive a JSON with requested language

Scenario: GET request for non-existent resource
Given <resource> not exists
When I send a request for <resource>
Then the request fails
  And I receive a relevant error message

| resource                  |
| list of language families |
| language family           |
| language                  |

Scenario: POST requests are disabled
When I send a POST request to the app
Then the request fails
