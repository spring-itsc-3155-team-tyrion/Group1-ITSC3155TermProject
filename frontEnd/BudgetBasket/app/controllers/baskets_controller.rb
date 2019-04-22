class BasketsController < ApplicationController
    def basket
        @baskets = Basket.all
    end
    
    def create
        @basket = Basket.new(basket_params)
        
        @basket.save
        redirect_to @basket
    end
    
    def destroy
        @basket = Basket.find(params[:id])
        @basket.destroy
        
        redirect_to basket_path
    end
    
    def calculation
        File.open(Dir.pwd + "/../../algorithms/library/data/ingredientModifiedList.list", "w") do |f|
            f.write("#ingredient_name\tingredient_count\tingredient_tag\n")
            for ingredient in Basket.pluck(:ingredient_name) do
                @basket = Basket.find_by(ingredient_name: ingredient)
                f.write((@basket.ingredient_name).to_s + "\t")
                f.write((@basket.ingredient_count).to_s + "\t")
                if @basket.ingredient_organic
                    f.write("organic")
                else
                    f.write("non-organic")
                end
                f.write("\n")
            end
        end
        
        system (Dir.pwd + '/../../algorithms/main.py')
        sleep(3)
    end
    
    def resetBasket
        @baskets = Basket.all
        @baskets.each do |ingredient|
            ingredient.destroy
        end
        
        @recipes = Recipe.all
        @recipes.each do |recipe|
            recipe.recipe_count_in_basket = 0
            recipe.save
        end
        
        redirect_to basket_path
    end
    
    def switchOrganicState
        @basket = Basket.find(params[:basket])
        @basket.ingredient_organic = !@basket.ingredient_organic
        @basket.save
        
        redirect_to basket_path
    end
end

private
    def basket_params
        params.require(:basket).permit(:ingredient_name, :ingredient_count, :ingredient_organic)
    end