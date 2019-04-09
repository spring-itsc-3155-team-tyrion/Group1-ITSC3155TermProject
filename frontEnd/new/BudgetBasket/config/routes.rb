Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
    get '/allRecipes' => 'recipes#allRecipes'
    get '/basket' => 'recipes#basket'
    get '/calculation' => 'recipes#calculation'
    root 'recipes#home'
end
