#!/usr/bin/env python

import os

### parameters
mainDir = os.getcwd()
ingredientList = 'ingredientModifiedList.sample'
routeTypes = ['bestPrice', 'leastNumStores']

try:
	print('\n-----Creating price matrix-----\n')
	from library.modules import createPriceMatrix
	priceMatrix = createPriceMatrix.__main__(mainDir, ingredientList)
	print('Done')
except Exception as e:
	print('Exception found during creating price matrix: ' + str(e))
	exit()

try:
	print('\n-----Creating coordinate matrix-----\n')
	from library.modules import createCoordinateMatrix
	coordinateMatrix = createCoordinateMatrix.__main__(mainDir)
	print('Done')
except Exception as e:
	print('Exception found during fetching store coordinates: ' + str(e))
	exit()
	
try:
	print('\n-----Calculating routes-----\n')
	from library.modules import calculateRoutes
	calculateRoutes.__main__(mainDir, priceMatrix, coordinateMatrix, routeTypes, ingredientList)
	print('Done')
except Exception as e:
	print('Exception found during calculating routes: ' + str(e))
print('')