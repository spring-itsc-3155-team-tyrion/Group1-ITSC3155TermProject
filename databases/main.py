#!/usr/bin/env python

import os

### parameters
mainDir = os.getcwd()
numStores = 4
numIngredients = (numStores + 1)*100
ingredientsList = 'ingredientsList.list'

try:
	print('\n------Creating ingredient list-----\n')
	from library.modules import createIngredientList
	createIngredientList.__main(mainDir, numIngredients, ingredientsList)
	print('Done')
except Exception as e:
	print('Exception found during creating of ingredient list: ' + str(e))
	exit()
