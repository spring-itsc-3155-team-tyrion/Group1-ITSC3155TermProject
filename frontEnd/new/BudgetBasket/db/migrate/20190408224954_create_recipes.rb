class CreateRecipes < ActiveRecord::Migration[5.2]
  def change
    create_table :recipes do |t|
      t.string :recipe_name
      t.text :recipe_ingredient_array

      t.timestamps
    end
  end
end
