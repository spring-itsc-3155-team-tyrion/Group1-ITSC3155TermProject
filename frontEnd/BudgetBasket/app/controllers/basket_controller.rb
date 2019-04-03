class BasketsController < ApplicationController
 
    #index of recipes in database
  def index
    #searches ingredients table and stores each row it finds in @baskets
    @baskets = Baskets.all
  end
  
  
  #after user chooses an ingredient, show displays info that was just entered into database
  def show
    #tell rails to find the ingredient with :id (when on page called by index, click link for specific ingredient, passes id of that ingredient via params)
    @basket = Basket.find(params[:id])
  end 
  
  
  #gets called when we display a page to the user to take their input (picking a ingredient)
  def new
    #creates new ingredient object
    @basket = Basket.new
    
    #grabs all ingredient from database and puts them in array called @baskets
    #not sure if this is how we want to implement the saved user ingredients
    @baskets = Baskets.all
  end 
 
 
   #saving data in the controller, record into database
  def create
    #creates new @basket var that holds an Ingredient object built from the data the user chose
    @basket = Basket.new(basket_params)
    
    #redirects user to index method if object saves correctly to database
    if @basket.save
      redirect_to :action => 'index'
    
    #if it doesnt save, user is sent back to the new method
    else
      #required in case it does not save data correctly
      @baskets = Baskets.all
      render :action => 'new'
    end 
  end 
  
  
  #called to display data on the screen to be modified by the user
  def edit
    #tell rails to find the ingredient with :id (when on page called by index, click link for specific ingredient, passes id of that ingredient via params)
    @basket = Basket.find(params[:id])
    
    #grabs all ingredients from database and puts them in array called @baskets
    @baskets = Baskets.all
  end 
  
  
  #called after edit method, when user modifies data and wants to update the changes into the database
  def update
    @basket = Basket.find(params[:id])
    
    #overwrites attributes of existing row in database, instead of creating a new row like create method
    if @basket.update_attributes(basket_params)
      redirect_to :action => 'show', :id => @basket
    else
      @baskets = Baskets.all
      render :action => 'edit'
    end 
  end 
  
  
  #delete a record from the database 
  def delete
    Basket.find(params[:id]).destroy
    redirect_to :action => 'index'
  end 
  
end

private
#whitelist code for other methods
#collects all the fields from object :baskets, data was passed from new method to create method using params object
def basket_params
    #ingredient database has 3 fields (ingredient_name, ingredient_price, ingredient_special_tag)
  params.require(:baskets).permit(:ingredient_name, :ingredient_price, :ingredient_special_tag)
end

    
    
