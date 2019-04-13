Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
    get '/allRecipes' => 'recipes#allRecipes'
    get '/basket' => 'baskets#basket'
    get '/calculation' => 'baskets#calculation'
    get 'button' => 'start_up#button'
    get 'addRecipeToBasketButton' => 'recipes#addRecipeToBasket'
    get 'deleteRecipeFromBasketButton' => 'recipes#deleteRecipeFromBasket'
    root 'recipes#home'
end
