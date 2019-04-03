class CreateBaskets < ActiveRecord::Migration[5.2]
  def change
    create_table :baskets do |t|
      t.string :ingredient_name
      t.float :ingredient_price
      t.boolean :ingredient_special_tag

      t.timestamps
    end
  end
end
