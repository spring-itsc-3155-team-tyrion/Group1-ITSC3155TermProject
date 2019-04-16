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
    end
    
    def switchOrganicState
        @basket = Basket.find(params[:basket])
        @basket.ingredient_organic = !@basket.ingredient_organic
        @basket.save
        
        redirect_to basket_path
    end
    
    def writeBasketActiveRecordToFile
        File.open("../../../..", "w+") do |f|
            f.write(puts "test")
        end
    end
end

private
    def basket_params
        params.require(:basket).permit(:ingredient_name, :ingredient_count, :ingredient_organic)
    end