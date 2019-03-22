# General runtime flow

###Screen_0 (index)###
## User is greeted by the home page
## User maybe clicks on the basket icon somewhere (top right hand corner of the screen maybe?)
## User is brought to Screen_1

###Screen_1###
## User queries unified database of available ingredients list and recipe list from a search bar feature (or something)
## User clicks on recipes or ingredients they want to add to their basket
## Recipes or ingredients that the user selected are inputted into a database
## For the sample this is called 'itemList.sample'
## User clicks 'done' button (or something) that brings them to Screen_2

###Backend intermediate###
## System should parse all of the ingredients from the item list database into a new database of ingredients and ingredient count
## System initializes all of the 'ingredient_tag' tags as 'null'
## For the sample this is called 'ingredientList.sample'

###Screen_2###
## User is presented with a full list of the ingredients in their basket
## User has the option to modify the counts of these ingredients (increment or decrement) or remove them all together
## User also has the option of putting a checkmark (or similar feature) next to any ingredient marking it as 'organic' to show preference
## System then stores information is a new database of ingredients with user modifications
## Any item that is not marked 'organic' is marked 'non-organic'
## For the sample this is called 'ingredientModifiedList.sample'
## User clicks 'done' button (or something) that brings them to the next screen in the next phase

# From here everything is done for the database team, I, Jacob, simply need this tab delimited file in the form of 'ingredientModifiedList.sample'
# Of course, the database teams needs to work out all of the logistics on how they want to take information from the samples databases
# and store data during runtime but this is the start point and end point laid out very clearly
# It is also worth noting that the intermediate files I used during the sample runtime, that being 'itemList.sample' and 'ingredientList.sample'
# is not how you want to store intermediate information during runtime, instead is should probably be stored using CRUD databses for Ruby on Rails
