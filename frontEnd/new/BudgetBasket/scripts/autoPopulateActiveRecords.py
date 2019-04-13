#!/usr/bin/env python

import os
from subprocess import Popen, PIPE, check_output

def __main__():
	wd = os.path.dirname(os.path.abspath( __file__ ))

	recipeDictionary = parseFile(wd + "/../../../../databases/library/data/recipes.list")
	ingredientDictionary = parseFile(wd + "/../../../../databases/library/data/availableIngredientList.list")

	os.chdir(wd + '/../')
	print(os.getcwd())

	destroyAllRecipeRecords()
	recordRecipes(recipeDictionary)
	recordIngredients(ingredientDictionary)

	print('Done')

def parseFile(file):
	with open(file, 'r') as chunk:
		dictionary = {}
		for line in chunk:
			if line.startswith('#'):
				pass
			else:
				dictionary[line.strip().split('\t')[0]] = line.strip().split('\t')[1:]
	chunk.close()

	return(dictionary)

def destroyAllRecipeRecords():
	print('Destroying all active record entries for Recipe')
	p1 = Popen(['echo', 'Recipe.destroy_all'], stdout=PIPE)
	p2 = Popen(['spring', 'rails', 'console'], stdin=p1.stdout, stdout=PIPE, stderr=open(os.devnull, 'w'))
	p1.stdout.close()
	output = p2.communicate()[0]

def recordRecipes(dictionary):
	for recipe in dictionary:
		print('Writing ' + str(recipe) + ' to active record Recipe')
		recipeName = recipe
		recipeIngredientArray = dictionary[recipe]
		arg = 'recipe=Recipe.create!(:recipe_name=>"' + recipeName + '",:recipe_ingredient_array=>' + str(recipeIngredientArray) + ')'
		p1 = Popen(['echo', arg], stdout=PIPE)
		p2 = Popen(['spring', 'rails', 'console'], stdin=p1.stdout, stdout=PIPE, stderr=open(os.devnull, 'w'))
		p1.stdout.close()
		output = p2.communicate()[0]

def recordIngredients(dictionary):
	for ingredient in dictionary:
		print('Writing ' + str(ingredient) + ' to active record Recipe')
		recipeName = ingredient
		recipeIngredientArray = [str(ingredient)]
		arg = 'recipe=Recipe.create!(:recipe_name=>"' + recipeName + '",:recipe_ingredient_array=>' + str(recipeIngredientArray) + ')'
                p1 = Popen(['echo', arg], stdout=PIPE)
                p2 = Popen(['spring', 'rails', 'console'], stdin=p1.stdout, stdout=PIPE, stderr=open(os.devnull, 'w'))
                p1.stdout.close()
                output = p2.communicate()[0]

__main__()
