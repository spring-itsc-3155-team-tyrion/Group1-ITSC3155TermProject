Feature: Add a recipe
  
  As a user
  So that I can easily use the application
  I want to be able to add a recipe
  
Scenario: As a user I want to be able to add a recipe to the basket
  Given I am on the allRecipes page
  When I click on the "addBtn" link
  Then I should visit the basket page
  And I should add a recipe to the basket