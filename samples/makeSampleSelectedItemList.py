#!/usr/bin/env python

import os
import random

def parseRecipes():
	with open('../databases/library/data/recipes.list', 'r') as chunk:
		recipeDictionary = {}
		recipe = []
		for line in chunk:
			if line.startswith('#'):
				pass
			else:
				recipe = line.strip().split('\t')
				recipeDictionary[recipe[0]] = recipe[1:]
	chunk.close()

	return(recipeDictionary)

def parseIngredients():
	with open('../databases/library/data/availableIngredientList.list', 'r') as chunk:
		ingredientList = []
		for line in chunk:
			if line.startswith('#'):
				pass
			else:
				ingredientList.append(line.split('\t')[0])
	chunk.close()

	return(ingredientList)
		

def writeRecipes(dictionary):
	with open(os.getcwd() + '/itemList.sample', 'w') as chunk:
		chunk.write('#item_name\tingredients\n')
		for recipe in dictionary:
			chunk.write(recipe)
			for ingredient in dictionary[recipe]:
				chunk.write('\t' + str(ingredient))
			chunk.write('\n')
	chunk.close()

recipeDictionary = parseRecipes()
ingredientList = parseIngredients()
sampleDictionaryKeys = random.sample(recipeDictionary, 10)
sampleIngredients = random.sample(ingredientList, 10)
sampleDictionary = {}
for key in sampleDictionaryKeys: sampleDictionary[key] = recipeDictionary[key]
for ingredient in sampleIngredients: sampleDictionary[ingredient] = [ingredient]
writeRecipes(sampleDictionary)
