#!/usr/bin/env python

import os
import random

def __main__(wd, availableIngredientList, maxIngredientsPerRecipe, numRecipes, recipesList):
	os.chdir(wd + '/library/data')

	with open(recipesList, 'w') as chunk:
		chunk.write('#recipe_name\tingredients\n')
		
		ingredientDictionary = parseAvailableIngredients(wd, availableIngredientList)
		
		for i in range(numRecipes):
			recipe = createRecipe(ingredientDictionary, maxIngredientsPerRecipe)
#			chunk.write('recipe_' + str(i))
			chunk.write('recipe_' + ('%0' + str(len(str(numRecipes))) + 'd') % i)
			for ingredient in recipe: chunk.write('\t' + ingredient)
			chunk.write('\n')
			
	chunk.close()

def parseAvailableIngredients(wd, input):
	os.chdir(wd + '/library/data')
	
	dict = {}
	with open(input, 'r') as file:
		for line in file:
			if line.startswith('#'): pass
			else: dict[line.strip().split('\t')[0]] = [line.strip().split('\t')[1], line.strip().split('\t')[2]]
	file.close()
	
	return(dict)

def createRecipe(ingredientDictionary, maxIngredientsPerRecipe):
	recipe = []
	for i in range(random.randint(2, maxIngredientsPerRecipe)): #asserts each recipe has at least 2 ingredients, max of specified ammount
		recipe += random.sample(ingredientDictionary.keys(), 1)
	
	return(recipe)
