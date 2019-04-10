class BasketsController < ApplicationController
    
    def basket
       # @baskets = Basket.all
    end
    
    def calculation
    end
    
    def create
        @basket = Basket.new(basket_params)
        
        @basket.save
        redirect_to @basket
    end
    
    def destroy
        @basket = Basket.find(params[:id])
        @basket.destroy
        
        redirect_to recipes_path
    end
end
