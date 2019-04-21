class AddRecipeCountInBaketToRecipe < ActiveRecord::Migration[5.2]
  def change
    add_column :recipes, :recipe_count_in_basket, :integer
  end
end
