#!/usr/bin/env python

import os

### parameters
mainDir = os.getcwd()
numStores = 4
numIngredientsPerStore = 100
numIngredientsTotal = numIngredientsPerStore + numStores*20 #20 extra ingredients per store
availableIngredientsList = 'availableIngredientList.list'

try:
	print('\n-----Creating availble ingredient list-----\n')
	from library.modules import createAvailableIngredientList
	createAvailableIngredientList.__main__(mainDir, numIngredientsTotal, availableIngredientsList)
	print('Done')
except Exception as e:
	print('Exception found during creating ingredient list: ' + str(e))
	exit()

try:
	print('\n-----Creating store catalogs----\n')
	from library.modules import createStoreCatalog
	for i in range(numStores): createStoreCatalog.__main__(mainDir, numIngredientsPerStore, i, availableIngredientsList, ('store' + str(i) + '.store'))
	print('Done')
except Exception as e:
	print('Exception found during creating store catalogs: ' + str(e))
	exit()
