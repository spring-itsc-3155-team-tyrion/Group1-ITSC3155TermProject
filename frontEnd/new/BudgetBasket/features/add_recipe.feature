Feature: Add a recipe

    As a user
    So that I can use the app
    I want to be able to add a recipe

Scenario: As a user I want to be able to navigate from the all recipes page to the basket page
    Given I am on the allRecipes page
    When I click the "basket" link
    Then I should be on the "basket" page
    And I should see the "switchOrganicState" field