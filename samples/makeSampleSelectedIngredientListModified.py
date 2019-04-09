#!/usr/bin/env python

import os
import random

def parseItems():
	with open('ingredientList.sample', 'r') as chunk:
		itemDictionary = {}
		for line in chunk:
			if line.startswith('#'):
				pass
			else:
				itemDictionary[line.strip().split('\t')[0]] = line.strip().split('\t')[1]

	chunk.close()

	return(itemDictionary)

def writeIngredientDictionary(dictionary):
	with open('ingredientModifiedList.sample', 'w') as chunk:
		chunk.write('#ingredient_name\tingredient_count\tingredient_tag\n')
		for key in dictionary:
			chunk.write(key)
			for item in dictionary[key]:
				chunk.write('\t' + str(item))
			chunk.write('\n')
	
	chunk.close()

ingredientDictionary = parseItems()
for item in ingredientDictionary.keys():
	if (random.randint(1,5) == 1):
		ingredientDictionary[item] = [ingredientDictionary[item],'organic']
	else:
		ingredientDictionary[item] = [ingredientDictionary[item],'non-organic']
writeIngredientDictionary(ingredientDictionary)
