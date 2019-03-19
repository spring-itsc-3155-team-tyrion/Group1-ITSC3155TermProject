#!/usr/bin/env python

import os
import random

def __main__(wd, numIngredientsPerStore, storeNum, availableIngredientList, storeFile):
	os.chdir(wd + '/library/data')

	with open(storeFile, 'w') as chunk:
		chunk.write('#store' + str(storeNum) + '\t' + '(' + str(random.randint(0,201)-100) + ',' + str(random.randint(0,201)-100) + ')\n')
		chunk.write('#ingredient_name\tingredient_price\tingredient_tag\n')
		
		parseAvailableIngredients(wd, availableIngredientList)

		#for i in range(numIngredientsPerStore): chunk.write()
	chunk.close()

def parseAvailableIngredients(wd, input):
	os.chdir(wd + '/library/data')
	
	ingredientDictionary = {}
	with open(input, 'r') as file:
		for line in file:
			if line.startswith('#'): pass
			else: print(line.strip().split('\t'))
			else: ingredientDictionary.add
	file.close()
