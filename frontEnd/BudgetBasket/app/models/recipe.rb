class Recipe < ApplicationRecord
    #has_many is 1-many connection with Baskets model
    has_many :baskets
end
