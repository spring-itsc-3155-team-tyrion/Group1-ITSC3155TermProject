#!/usr/bin/env python

import os

def parseSampleRecipes():
	with open('itemList.sample', 'r') as chunk:
		recipeDictionary = {}
		for line in chunk:
			if line.startswith('#'):
				pass
			else:
				recipeDictionary[line.strip().split('\t')[0]] = line.strip().split('\t')[1:]
	chunk.close()

	return(recipeDictionary)

def getIngredientDictionary(dictionary):
	ingredientDictionary = {}
	for key in dictionary:
		for ingredient in dictionary[key]:
			if ingredient in ingredientDictionary.keys():
				ingredientDictionary[ingredient] += 1
			else:
				ingredientDictionary[ingredient] = 1


	return(ingredientDictionary)

def writeIngredientDictionary(dictionary):
	with open('ingredientList.sample', 'w') as chunk:
		chunk.write('#ingredient_name\tingredient_count\tingredient_tag\n')
		for key in dictionary:
			chunk.write(key + '\t' + str(dictionary[key]) + '\t' + 'null' + '\n')

	chunk.close()

recipeDictionary = parseSampleRecipes()
ingredientDictionary = getIngredientDictionary(recipeDictionary)
writeIngredientDictionary(ingredientDictionary)
