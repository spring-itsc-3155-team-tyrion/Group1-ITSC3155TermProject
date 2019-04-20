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
    
    def resetRecipeCounts
        @baskets = Basket.all
        @baskets.each do |recipe|
            recipe.destroy
        end
        
        redirect_to allRecipes_path
    end
    
    def addRecipeToBasket
        @recipe = Recipe.find(params[:recipe])
        
        for ingredient in @recipe.recipe_ingredient_array do
            if Basket.exists?(ingredient_name: ingredient)
                @basket = Basket.find_by(ingredient_name: ingredient)
                @basket.ingredient_count = @basket.ingredient_count + 1
                @basket.save
            else
                @basket = Basket.new(:ingredient_name => ingredient, :ingredient_count => 1, :ingredient_organic => false)
                @basket.save
            end
        end
        
        redirect_to allRecipes_path
    end
    
    def deleteRecipeFromBasket
        @recipe = Recipe.find(params[:recipe])
        system ("echo 'delete recipe '" + @recipe.recipe_name)
        
        redirect_to allRecipes_path
    end
end

private
    def recipe_params
        params.require(:recipe).permit(:recipe_name, :recipe_ingredient_array)
    end