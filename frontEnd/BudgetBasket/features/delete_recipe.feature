Feature: Delete a recipe
  
  As a user
  So that I can easily use the application
  I want to be able to delete a recipe
  
Scenario: As a user I want to be able to delete a recipe from the basket
  Given I am on the allRecipes page
  When I click on the "deleteBtn" link
  Then I should visit the basket page
  And I should delete a recipe from the basket