Given("I click the deleteBtn") do
    click_link deleteBtn
end

Then("I should visit the basket page") do
    vist basket_path 
end

Then("I should delete a recipe from the basket") do
    
end