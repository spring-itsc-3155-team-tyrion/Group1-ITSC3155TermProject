#!/usr/bin/env python

import os
import itertools
import math

def __main__(wd, priceMatrix, coordinateMatrix, routeTypes, ingredientList):
    os.chdir(wd + '/../samples')

    ingredientDictionary = parseIngredientList(ingredientList) #{ingredient_name: ingredient_count}
    
    for routeType in routeTypes:
        if routeType == "bestPrice": #absolute best price at store, does not take into account travel expenses, possible feature later on
            information = getInformation_bestPrice(priceMatrix, ingredientDictionary)
            storeWithBestPriceMatrix = information['storeWithBestPriceMatrix']
            completelyUnavailableIngredients = information['completelyUnavailableIngredients']
            substitutedIngredients = information['substitutedIngredients']
            
            print('Total Number of Ingredients: ' + str(len(ingredientDictionary.keys())) + ' (Should be the number of completelyUnavailableIngredients + number of found original ingredients)\n')    
            print('Number of found original ingredients (storeWithBestPriceMatrix): ' + str(len(storeWithBestPriceMatrix.keys())))
            print(storeWithBestPriceMatrix)
            print('\n')
            print('Number of completelyUnavailableIngredients: ' + str(len(completelyUnavailableIngredients)))
            print(completelyUnavailableIngredients)
            print('\n')
            print('Number of substitutedIngredients: ' + str(len(substitutedIngredients)))
            print(substitutedIngredients)
            
            results = calculateRoute_bestPrice(coordinateMatrix, storeWithBestPriceMatrix)
            shortestPermutation = results[0]
            shortestPermutationDistance = results[1]
            
            print(shortestPermutation)
            print(shortestPermutationDistance)
            
        elif routeType == "leastNumStores":
            getInformation_leastNumStores(priceMatrix, coordinateMatrix, ingredientDictionary)
            calculateRoute_leastNumStores(priceMatrix, coordinateMatrix, ingredientDictionary)
        else:
            print("RouteType not programmed!")
            
            
def getInformation_bestPrice(priceMatrix, ingredientDictionary):
    bestPrice = 10000000 #set to a very large number so first price found is always best price
    completelyUnavailableIngredients = [] #elements in this list have both organic and non-organic versions unavailable in all stores
    substitutedIngredients = [] #elements in this list were originally unavailable, however their opposite ingredient (organic --> non-organic, non-organic --> organic) was available, then that new version was added to the storeWithBestPriceMatrix, so for example, if ingredient_137_organic is in the list, then ingredient_137_non-organic is the storeWithBestPriceMatrix, and ingredient_137_organic was what the user orginally requested
    storeWithBestPriceMatrix = {}
    
    for ingredient in ingredientDictionary:
        
        for store in priceMatrix: #checks all stores for originally selected ingredient
            if ingredient in priceMatrix[store].keys():
                if float(priceMatrix[store][ingredient]) < bestPrice: #currently doesnt have any added functionality if two stores just so happen to have the same price, this might be added in the future
                    bestPrice = priceMatrix[store][ingredient]
                    storeWithBestPriceMatrix[ingredient] = store
            else:
                pass
        
        oppositeIngredient = ''
        if ingredient not in storeWithBestPriceMatrix.keys(): #if origincally selected ingredient was not found, checks all stores for opposite ingredient a.k.a., ingredient_003_non-organic --> ingredient_003_organic and vice versa
            if 'non' in ingredient:
                oppositeIngredient = ingredient.split('_')[0] + '_' + ingredient.split('_')[1] + '_organic'
            else:
                oppositeIngredient = ingredient.split('_')[0] + '_' + ingredient.split('_')[1] + '_non-organic'
            
            for store in priceMatrix:    
                if oppositeIngredient in priceMatrix[store].keys():
                        if float(priceMatrix[store][oppositeIngredient]) < bestPrice:
                            bestPrice = priceMatrix[store][oppositeIngredient]
                            storeWithBestPriceMatrix[oppositeIngredient] = store
                        else:
                            pass
        
        if ingredient not in storeWithBestPriceMatrix.keys() and oppositeIngredient not in storeWithBestPriceMatrix.keys():
            completelyUnavailableIngredients.append(ingredient)
        
        if oppositeIngredient in storeWithBestPriceMatrix.keys():
            substitutedIngredients.append(ingredient)
    
    return({'storeWithBestPriceMatrix': storeWithBestPriceMatrix, 'completelyUnavailableIngredients': completelyUnavailableIngredients, 'substitutedIngredients': substitutedIngredients})
    

#this looks at raw store prices, not the user quantity (AKA this metho assumes that the user selected one of every item in list)
def calculateRoute_bestPrice(coordinateMatrix, storeWithBestPriceMatrix): #this method generates one defined root to be the shortest where in all actuality for every route, there is an identical, reverse route. It is arbitrary which is selected. So if there are n routes generated, there are n/2 unique routes.
    stores = []
    for key in storeWithBestPriceMatrix:
        if storeWithBestPriceMatrix[key] in stores:
            pass
        else:
            stores.append(storeWithBestPriceMatrix[key])
    
    coordinateMatrix['origin'] = ['0','0']
    
    distanceDict = {}
    counter = 0
    for permutation in list(itertools.permutations(stores)):
        permutation = list(permutation)
        permutation.insert(0, 'origin')
        permutation.append('origin')
        
        totalDistance = 0
        for i in range(0,len(permutation)-1):
            #print(str(permutation[i]) + ' --> ' + str(permutation[i+1]))
            distance = getDistance(coordinateMatrix[permutation[i]], coordinateMatrix[permutation[i+1]])
            #print(distance)
            totalDistance += distance
            
        distanceDict['permutation_' + str(counter)] = [permutation,totalDistance]
        counter += 1
    
    shortestPermutationNum = ''
    shortestDistance = 10000000 #set to a very large number so first distance is always the shortest
    for p in distanceDict:
        if distanceDict[p][1] < shortestDistance:
            shortestPermutationNum = p
            shortestDistance = distanceDict[p][1]
    
    return(distanceDict[shortestPermutationNum])

def getDistance(pointA, pointB):
    distance = math.sqrt((float(pointB[0]) + float(pointA[0]))**2 + (float(pointB[1]) + float(pointA[1]))**2)
    
    return(distance)
    
def getInformation_leastNumStores(priceMatrix, coordinateMatrix, ingredientDictionary):
    print('')
    
def calculateRoute_leastNumStores(priceMatrix, coordinateMatrix, ingredientDictionary):
    print('')
    
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
