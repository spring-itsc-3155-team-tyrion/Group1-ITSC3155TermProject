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
        
        countArray = []
        #fill countArray which tracks number of occurences of ingredients in basket (varifies that the recipe was actually added to the basket)
        for ingredient in @recipe.recipe_ingredient_array do
            if Basket.exists?(ingredient_name: ingredient)
                @basket = Basket.find_by(ingredient_name: ingredient)
                countArray[countArray.length] = @basket.ingredient_count
            else
                countArray[countArray.length] = 0
            end
        end
        
        system ("echo " + countArray.to_s)
        system ("echo " + (countArray.min).to_s)
        
        if countArray.min != 0
            for ingredient in @recipe.recipe_ingredient_array do
                if Basket.exists?(ingredient_name: ingredient)
                    @basket = Basket.find_by(ingredient_name: ingredient)
                    @basket.ingredient_count = @basket.ingredient_count - 1
                    @basket.save
                    if @basket.ingredient_count == 0
                        @basket.destroy
                    end
                else
                    system ("echo " + "critical erorr in deleteRecipeFromBasket method")
                end
            end
        else
            system ("echo " + "user tried deleting a recipe that was never added to the basket")
        end
        
        redirect_to allRecipes_path
    end
end

private
    def recipe_params
        params.require(:recipe).permit(:recipe_name, :recipe_ingredient_array)
    end