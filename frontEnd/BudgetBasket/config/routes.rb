Rails.application.routes.draw do
  get '/allRecipes' => 'recipes#allRecipes'
  get '/basket' => 'recipes#basket'
  get '/calculation' => 'recipes#calculation'
  root 'recipes#home'
  
  
  
  
  
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
