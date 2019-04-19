class CreateBaskets < ActiveRecord::Migration[5.2]
  def change
    create_table :baskets do |t|
      t.string :ingredient_name
      t.integer :ingredient_count
      t.boolean :ingredient_organic

      t.timestamps
    end
  end
end
