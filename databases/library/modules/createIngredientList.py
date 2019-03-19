#!/usr/bin/env python

import os

def __createIngredientList__(wd, numIngredients, ingredientsListFile):
	os.chdir(wd + '/library/data')

	with open(ingredientsListFile, 'w') as chunk:
		for i in range(numIngredients): chunk.write('ingredient_' + ('%0' + str(len(str(numIngredients))) + 'd') % i + '\n')
	chunk.close()
