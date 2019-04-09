#!/usr/bin/env python

import os
import re

def __main__(wd, ingredientList):
	os.chdir(wd + '/../../../samples')

	ingredientDictionary = parseIngredientList(ingredientList)

	collectiveStoreDictionary = {}
	storeDirectory = os.listdir(wd + '/../../../databases/library/data/')
	numStores = 0
	for item in storeDirectory:
		if item.startswith("store"):
			numStores += 1
		else:
			pass

	for i in range(0,numStores):
		collectiveStoreDictionary[i] = getStorePriceDictionary(wd + '/../../../databases/library/data/store' + str(i) + '.store')

	print(collectiveStoreDictionary[0]['ingredient_007']) #this prints the price and special tag for 'ingredient_007' from store 0

	writeStoreMatrix(collectiveStoreDictionary, ingredientDictionary):
		

def parseIngredientList(ingredientList):
	with open(ingredientList, 'r') as chunk:
		ingredientDictionary = {}
		for line in chunk:
			if line.startswith('#'):
				pass
			else:
				ingredientDictionary[line.strip().split('\t')[0]] = line.strip().split('\t')[1:]
	chunk.close()

	return(ingredientDictionary)


def getStorePriceDictionary(store):
	with open(store, 'r') as chunk:
		storeDictionary = {}
		for line in chunk:
			if line.startswith('#'):
				pass
			else:
				storeDictionary[line.strip().split('\t')[0]] = line.strip().split('\t')[1:]
	chunk.close()

	return(storeDictionary)
