Feature -> Guest

As a guest
I would like to be able to explore the website without logging in
So that I can quickly find out whether it’s something I’m interested in

Background
Given I am not logged in
  And I can see a generic greeting
  And I can proceed to login page

Scenario: User without login arrives at homepage
Given I am on homepage
Then I can see a Call To Action element
  And I can select an existing language family
  And I can see option to add language family


Scenario: User without login tries to add language family
Given I am on homepage
When I try to add a language family
Then I am directed to login page


Scenario: User without login views language family page
Given I am on a language family page
Then I can see a list of languages
  And I can see a language group description
  And I can proceed to a language page
  And I can go back to homepage


Scenario: User without login uses options menu
Given I am on a language family page
  And I open the options menu
When I select <option>
Then I am directed to login page

Examples:
| option           |
| Add new language |
| Edit language    |
| Delete language  |


Scenario: User views language page
Given I am on a language page
Then I can see a language description
  And I can see a list of language trivia
  And I can see a list of learning tips
  And I can proceed to Wikipedia articles on the phonology, dialects and grammar of the language
  And I can go back to language family page
