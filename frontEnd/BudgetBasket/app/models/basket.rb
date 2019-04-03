class Basket < ApplicationRecord
       #belongs_to creates a 1-1 connection with recipe model, must use singular term
        belongs_to :recipe
end
