require 'rails_helper.rb'

feature "User adds a recipe" do
    scenario "User successfully navigates to the basket page from the recipes page" do
        visit allRecipes_path
        expect(page).to have_content("allRecipes")
        click_link "Add Recipe(s) to Basket"
        expect(page).to have_content("basket")
    end
end
    