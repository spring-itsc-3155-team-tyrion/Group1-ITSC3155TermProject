Given("I click the Empty Basket link") do
    click_link resetBasket
end

Then("I should empty the basket") do
    visit basket_path
end