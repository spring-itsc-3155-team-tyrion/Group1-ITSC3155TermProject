class OrderedRecipeQuery
    
    #.freeze makes object called immutable
    SORT_OPTIONS = %w(by_ingredient_name by_ingredient_price by_ingredient_tag).freeze
    
    #might need to change :user var
    def initialize(params = {}, relation = Recipe.includes(:user))
        @relation = relation
        @params = params
    end
   
   def all
       @relation.public_send(sort_by, direction)
   end
   
   #method for storing user selected recipe
   def userSelect
       #need variable for w/e user selects
       #if statement for when user selects it
       #create a new variable to store whatever user picks
       #something like the following?
       Recipe.all.each do |user|
           @recipechoice = Recipe.all(user) #:user ?
           
       end
   end
   
   private
   
   def sort_by
       @params[:sort].presence_in(SORT_OPTIONS) || :by_ingredient_name
        #might need to have different @params for each individual ingredient tag?
   end
   
   def direction
       #ascending/descending order (set to asc?)
       @params[:direction] == "asc" ? :asc : :desc
   end
   
   
   
end