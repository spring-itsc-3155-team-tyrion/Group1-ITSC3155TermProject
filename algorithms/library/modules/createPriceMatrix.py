#!/usr/bin/env python

import os
import re

def __main__(wd, ingredientList):
	os.chdir(wd + '/../samples')

	ingredientDictionary = parseIngredientList(ingredientList) #{ingredient_name: ingredient_count}

	collectiveStoreDictionary = {} #{store_num: {ingredient_name: ingredient_price}}
	storeDirectory = os.listdir(wd + '/../databases/library/data/')
	numStores = 0
	for item in storeDirectory:
		if item.startswith("store"):
			numStores += 1
		else:
			pass

	for i in range(0,numStores):
		collectiveStoreDictionary['store_' + str(i)] = getStorePriceDictionary(wd + '/../databases/library/data/store' + str(i) + '.store')

	#print(collectiveStoreDictionary['store_0']['ingredient_007_non-organic']) #this prints the price and special tag for 'ingredient_007_non-organic' from store store_0
	
	return(collectiveStoreDictionary)
		

def parseIngredientList(ingredientList):
	with open(ingredientList, 'r') as chunk:
		ingredientDictionary = {}
		for line in chunk:
			if line.startswith('#'):
				pass
			else:
				ingredientDictionary[line.strip().split('\t')[0] + '_' + line.strip().split('\t')[2]] = line.strip().split('\t')[1]

	chunk.close()

	return(ingredientDictionary)


def getStorePriceDictionary(store):
	with open(store, 'r') as chunk:
		storeDictionary = {}
		for line in chunk:
			if line.startswith('#'):
				pass
			else:
				storeDictionary[line.strip().split('\t')[0] + '_' + line.strip().split('\t')[2]] = line.strip().split('\t')[1]
				
	chunk.close()

	return(storeDictionary)
