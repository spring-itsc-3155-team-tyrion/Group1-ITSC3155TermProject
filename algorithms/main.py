#!/usr/bin/env python

import os

### parameters
mainDir = os.getcwd()
ingredientList = 'ingredientModifiedList.sample'

try:
	print('\n-----Creating price matrix -----\n')
	from library.modules import createPriceMatrix
	createPriceMatrix.__main__(mainDir, ingredientList)
	print('Done')
except Exception as e:
	print('Exception found during creating price matrix: ' + str(e))
	exit()

print('')
