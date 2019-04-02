class RecipesController < ApplicationController
    def home
        #this was one of sarahs methods
    end

   #index of recipes in database
  def index
    #searches recipes table and stores each row it finds in @recipes
    @recipes = Recipe.all
  end
  
  
  #after user chooses recipe, show displays info that was just entered into database
  def show
    #tell rails to find the recipe with :id (when on page called by index, click link for specific recipe, passes id of that recipe via params)
    @recipe = Recipe.find(params[:id])
  end 
  
  
  #gets called when we display a page to the user to take their input (picking a recipe)
  def new
    #creates new recipe object
    @recipe = Recipe.new
    
    #grabs all recipes from database and puts them in array called @recipes
    #not sure if this is how we want to implement the saved user recipes
    @recipes = Recipes.all
  end 
 
 
   #saving data in the controller, record into database
  def create
    #creates new @recipe var that holds a Recipe object built from the data the user chose
    @recipe = Recipe.new(params[:recipe])
    
    #redirects user to index method if object saves correctly to database
    if @recipe.save
      redirect_to :action => 'index'
    
    #if it doesnt save, user is sent back to the new method
    else
      #required in case it does not save data correctly
      @recipes = Recipes.all
      render :action => 'new'
    end 
  end 
  
  
  #called to display data on the screen to be modified by the user
  def edit
    #tell rails to find the recipe with :id (when on page called by index, click link for specific recipe, passes id of that recipe via params)
    @recipe = Recipe.find(params[:id])
    
    #grabs all recipes from database and puts them in array called @recipes
    @recipes = Recipes.all
  end 
  
  
  #called after edit method, when user modifies data and wants to update the changes into the database
  def update
    @recipe = Recipe.find(params[:id])
    
    #overwrites attributes of existing row in database, instead of creating a new row like create method
    if @recipe.update_attributes(recipe_params)
      redirect_to :action => 'show', :id => @recipe
    else
      @recipes = Recipes.all
      render :action => 'edit'
    end 
  end 
  
  
  #delete a record from the database 
  def delete
    Recipe.find(params[:id]).destroy
    redirect_to :action => 'index'
  end 
  
end

private
#whitelist code for other methods
#collects all the fields from object :recipes, data was passed from new method to create method using params object
def recipe_params
  #currently our recipe database only has 2 fields (recipe_name and ingredients), not sure if we will add more params to this or not
  params.require(:recipes).permit(:recipe_name, :ingredients)
end

end
