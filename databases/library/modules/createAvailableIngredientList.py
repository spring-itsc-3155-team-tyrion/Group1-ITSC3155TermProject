#!/usr/bin/env python

import os
import random

def __main__(wd, numIngredients, availableIngredientsListFile):
	os.chdir(wd + '/library/data')

	with open(availableIngredientsListFile, 'w') as chunk:
		chunk.write('#ingredient_name\tingredient_price\tingredient_special_tag\n')
		for i in range(numIngredients): chunk.write('ingredient_' + ('%0' + str(len(str(numIngredients))) + 'd') % i + '\t'
			+ str(float(random.randint(1, 1001))/100.00) + '\t' + 'null' + '\n')
	chunk.close()
