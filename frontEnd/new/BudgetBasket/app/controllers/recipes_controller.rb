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
        
        redirect_to allRecipes_path
    end
    
    def addRecipeToBasket
        @recipe = Recipe.find(params[:recipe])
        #system (Dir.pwd + '/scripts/addRecipeToBasket.py')
        system ("echo 'add recipe '" + @recipe.recipe_name)
        
        redirect_to allRecipes_path
    end
    
    def deleteRecipeFromBasket
        @recipe = Recipe.find(params[:recipe])
        #system (Dir.pwd + '/scripts/deleteRecipeFromBasket.py')
        system ("echo 'delete recipe '" + @recipe.recipe_name)
        
        redirect_to allRecipes_path
    end
end

private
    def recipe_params
        params.require(:recipe).permit(:recipe_name, :recipe_ingredient_array)
    end