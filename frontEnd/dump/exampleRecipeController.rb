class RecipeController < ApplicationController
    
    #modelled most of this from our blog app, probably wont need/might alter the show/new/create etc
    
    def index
        @recipes = OrderedRecipeQuery.new(sort_query_params).all.page(params[:page])
    end
    
    def show
        @recipe = Recipe.find(params[:id])
    end
    
    def new
        @recipe = Recipe.new
    end 
    
    
    def create
        #need to initialize recipe_params vv below
        @recipe = Recipe.new(recipe_params)
        #byebug
        
        if @recipe.save
            #byebug
            redirect_to @recipe
        else
            render 'new'
        end
    end
    
    def edit
        @recipe = Recipe.find(params[:id])
    end
    
    def update
        @recipe = Recipe.find(params[:id])
        
            if @recipe.update(recipe_params)
                redirect_to @recipe
            else
                render 'edit'
            end
    end
    
    def destroy
        @recipe = Recipe.find(params[:id])
        @recipe.destroy
        
        #need recipe_path vvvvv
        redirect_to articles_path
    end
    
end

private
    #recipe_params will have ingredient_name, ingredient_price, ingredient_tag
    def recipe_params
        params.require(:recipe).permit(:ingredient_name, :ingredient_price, :ingredient_tag)
    end

    def sort_query_params
        #slice:Returns a new ActionController::Parameters instance that includes only the given keys. If the given keys don’t exist, returns an empty hash.
        params.slice(:sort_by, :direction)
    end
