#!/usr/bin/env python

import os

### parameters
mainDir = os.path.dirname(os.path.abspath(__file__))
ingredientList = 'ingredientModifiedList.list'
travelCostPerUnit = 0.01 #arbitrary price for distance of arbitrary units
routeTypes = ['bestPriceAtStore', 'leastNumStores', 'bestPriceTravelAndStore']
#description of routes:
#
### bestPriceAtStore: This algorithm first finds the store of availability where
### the ingredient is cheapest. It then constructs a store with best price
### matrix which maps the store of lowest price with every ingredient. Then,
### as travel expenses are not taken into account, a TSP calculation is
### performed to determine the route. Shortcommings of this route include the
### fact that the route does not incorporate travel expenses. An implementation
### of this feature must deterministically permute not only the ingredient
### prices at every store, but must intrinsically treat every ingredient as its
### true count, not as a single element. To illustrate this point, say store_1
### sold ingredient_001 for 2.54 and ingredient_015 4.62 whereas store_2
### sold ingredient_001 for 2.55 and ingredient_015 0.10. Immediate observation
### suggests that purchasing both items at store_2 would be the best option.
### However this assumes the user only wants one of each ingredient. Suppose
### the user wanted 100000000 of ingredient_0001, though an extreme example, 
### serves to demonstrate the fact that the decision to go to store_2 would
### change based on the quantity metric of ingredients. Current algorithm does
### not implement this, but, as all stores have relatively similar prices and 
### the user hopefully does not want an absurd quantitiy of a given ingredient,
### the algorithm's innacurate guess is in all actuallity likely fairly
### accurate.
#
### leastNumStores: 
#
### bestPriceTravelAndStore:

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
	calculateRoutes.__main__(mainDir, priceMatrix, coordinateMatrix, routeTypes, ingredientList, travelCostPerUnit)
	print('Done')
except Exception as e:
	print('Exception found during calculating routes: ' + str(e))
print('')