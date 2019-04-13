class BasketsController < ApplicationController
    def allBaskets
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
        
        redirect_to baskets_path
    end
    
    def switchOrganicState
        @basket = Basket.find(params[:id])
        @basket.ingredient_organic = !@basket.ingredient_organic
        
        redirect_to baskets_path
    end
end

private
    def basket_params
        params.require(:basket).permit(:ingredient_name, :ingredient_count, :ingredient_organic)
    end