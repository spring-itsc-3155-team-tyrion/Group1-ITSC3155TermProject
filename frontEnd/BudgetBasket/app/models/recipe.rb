class Recipe < ApplicationRecord
    serialize :recipe_ingredient_array,Array
end
