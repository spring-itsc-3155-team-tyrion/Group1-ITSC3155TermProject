#!/usr/bin/env python

import os
import random

def __main__(wd, organicPriceMultiplier, priceVariance, chanceToBeOrganic, numIngredientsPerStore, storeNum, availableIngredientList, storeFile):
	os.chdir(wd + '/library/data')

	with open(storeFile, 'w') as chunk:
		chunk.write('#store' + str(storeNum) + '\t' + '(' + str(random.randint(0,201)-100) + ',' + str(random.randint(0,201)-100) + ')\n')
		chunk.write('#ingredient_name\tingredient_price\tingredient_tag\n')
		
		ingredientDictionary = parseAvailableIngredients(wd, availableIngredientList)
		sample = random.sample(ingredientDictionary, numIngredientsPerStore)

		#for ingredient in sample: chunk.write(str(ingredient) + '\t' + str(float(random.randint(ingredientDictionary[ingredient][1]*90,ingredientDictionary[ingredient][1]*110))/100.00) + '\n')
		for ingredient in sample:
			minPrice = float(ingredientDictionary[ingredient][0])*(float(100 - priceVariance)/100.00)
			maxPrice = float(ingredientDictionary[ingredient][0])*(float(100 + priceVariance)/100.00)
			randomPrice = float(random.randint(int(minPrice*1000), int(maxPrice*1000))/1000.00)
			chunk.write(ingredient + '\t' + str(randomPrice) + '\t' + 'non-organic' + '\n')
			
			if (random.randint(1,100) <= chanceToBeOrganic):
				chunk.write(ingredient + '\t' + str(randomPrice * float(organicPriceMultiplier)) + '\t' + 'organic' + '\n')
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
