Feature: Navigate from home page to allRecipes page
  
  As a user
  So that I can easily navigate my app
  I want to navigate from the home page to the allRecipes page
  
  Scenario: As a user I want to be able to navigate from the home page to the allRecipes page
    Given I am on the home page
    When I click on the "Check Out Our Recipes" link
    Then I should be on the "All Recipes" page
    
  Scenario: As a user I want to be able to navigate from the allRecipes page to the basket page
    Given I am on the allRecipes page
    When I click on the "Add Recipe(s) to Basket" link
    Then I should be on the "Basket Ingredients" page
   
    
