Feature -> Logged-in user

As a logged-in user
I would like to be able to add, read and modify language related content on the website
So that I can share my knowledge and passion for languages and learn from others

Background:
Given I am logged in
  And I can see a personalised greeting
  And I can log out
  But I cannot proceed to Login page


Scenario: Logged-in user arrives at homepage
Given I am on homepage
Then I can see a Call To Action element
  And I can select an existing language family
  And I can see option to add language family


Scenario: Logged-in user tries to add language family
Given I am on homepage
When I try to add a language family
Then I am directed to Add Family page


Scenario: Logged-in user adds/edits language family
Given I am on <page>
When I enter family name
  And I enter family description
  And I submit form
Then I am directed to homepage
  And I can see a success message
  And I can see the newly <result> language family

Examples:
| page             | result |
| Add Family page  | added  |
| Edit Family page | edited |


Scenario: Logged-in user views language family page
Given I am on a language family page
Then I can see a list of languages
  And I can see a language group description
  And I can proceed to a language page
  And I can go back to homepage


Scenario: Logged-in user uses options menu
Given I am on a language family page
  And I can see the options menu
When I select <option>
Then I am directed to <page>

Examples:
| option                  | page                        |
| Add new language        | Add Language page           |
| Delete language         | Delete Language page        |
| Edit language           | Edit Language page          |
| Delete language family  | Delete Language family page |
| Edit language family    | Edit Language family page   |


Scenario: Logged-in user adds/edit language
Given I am on <page>
When I enter language name
  And I enter language description
  And I enter language trivium
  And I enter language learning tip
  And I submit form
Then I am directed to relevant language family page
  And I can see a success message
  And I can see the newly <result> language

Examples:
| page               | result |
| Add Language page  | edited |
| Edit Language page | added  |


Scenario: Logged-in user deletes language/language family
Given I am on <page>
When I confirm I want to delete <deleted_entity>
Then I am directed to <redirect_page>
  And I can see a success message
  And I should not see the newly deleted <deleted_entity>

Examples:
| page                        | deleted_entity  | redirect_page                 |
| Delete Language page        | languge         | relevant language family page |
| Delete Language Family page | language family | homepage                      |


Scenario: User views language page
Given I am on a language page
Then I can see a language description
  And I can see a list of language trivia
  And I can see a list of learning tips
  And I can proceed to Wikipedia articles on the phonology, dialects and grammar of the language
  And I can go back to language family page


Scenario: User logs out
When I log out
Then I am not logged in
