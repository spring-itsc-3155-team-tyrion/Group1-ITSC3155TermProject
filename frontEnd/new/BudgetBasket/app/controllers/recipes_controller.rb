class RecipesController < ApplicationController
    def allRecipes
        @recipes = Recipe.all
    end
    
    def create
        @recipe = Recipe.new(recipe_params)
        
        @recipe.save
        redirect_to @recipe
    end
    
    def destroy
        @recipe = Recipe.find(params[:id])
        @recipe.destroy
        
        redirect_to recipes_path
    end
    
    def addRecipeToBasket()
        system (Dir.pwd + '/scripts/addRecipeToBasket.py')
        
        redirect_to recipe_path
    end
    
    def deleteRecipeFromBasket()
        system (Dir.pwd + '/scripts/deleteRecipeFromBasket.py')
        
        redirect_to recipe_path
    end
end

private
    def recipe_params
        params.require(:recipe).permit(:recipe_name, :recipe_ingredient_array)
    end