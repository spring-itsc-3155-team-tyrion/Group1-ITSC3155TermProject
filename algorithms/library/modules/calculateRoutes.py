#!/usr/bin/env python

import os
import itertools
import math
import json

def __main__(wd, priceMatrix, coordinateMatrix, routeTypes, ingredientList, travelCostPerUnit):
    os.chdir(wd + '/library/data')
    
    if 'data.json' in os.listdir(wd + '/../frontEnd/BudgetBasket/app/assets'): os.remove(wd + '/../frontEnd/BudgetBasket/app/assets/data.json')
    
    ingredientDictionary = parseIngredientList(ingredientList) #{ingredient_name: ingredient_count}
    
    for routeType in routeTypes:
        print('--------->Calculating route type ' + routeType + '\n')
        
        if routeType == "bestPriceAtStore": #absolute best price at store, does not take into account travel expenses, possible feature later on
            information = getInformation_bestPriceAtStore(priceMatrix, ingredientDictionary)
            storeWithBestPriceMatrix = information['storeWithBestPriceMatrix']
            completelyUnavailableIngredients = information['completelyUnavailableIngredients']
            substitutedIngredients = information['substitutedIngredients']
            
            '''
            print('Total Number of Ingredients: ' + str(len(ingredientDictionary.keys())) + ' (Should be the number of completelyUnavailableIngredients + number of found original ingredients)\n')    
            print('Number of found original ingredients (storeWithBestPriceMatrix): ' + str(len(storeWithBestPriceMatrix.keys())))
            print('##This matrix will only contain originally selected user ingredient names and substituted ingredient names that are opposite to the elements in the substitutedIngredients array')
            print(storeWithBestPriceMatrix)
            print('\n')
            print('Number of completelyUnavailableIngredients: ' + str(len(completelyUnavailableIngredients)))
            print('##This array will only contain originally selected user ingredient names, where the ingredient was not found in any store in the organic or non-organic form')
            print(completelyUnavailableIngredients)
            print('\n')
            print('Number of substitutedIngredients: ' + str(len(substitutedIngredients)))
            print('##This array will only contain originally selected user ingredient names, where the ingredient was not found in any store in the user selected form, but was found in the opposite form')
            print(substitutedIngredients)
            print('\n')
            '''
            
            results = calculateRoute_bestPriceAtStore(coordinateMatrix, storeWithBestPriceMatrix)
            shortestPermutation = results[0]
            shortestPermutationDistance = results[1]
            totalTravelCost = float(shortestPermutationDistance) * float(travelCostPerUnit)
            
            totalCost = getTotalPrice_bestPriceAtStore(storeWithBestPriceMatrix, priceMatrix, ingredientDictionary, totalTravelCost)
            
            print('Results:')
            print('optimal route: ' + str(shortestPermutation))
            print('route distance: ' + str(shortestPermutationDistance))
            print('price of travel: ' + str(totalTravelCost))
            print('price of ingredients: ' + str(totalCost-totalTravelCost))
            print('total price: ' + str(totalCost))
            
            shoppingList = getShoppingList(storeWithBestPriceMatrix, priceMatrix, ingredientDictionary)
            
            outputDictionary = {}
            outputDictionary['route_order'] = shortestPermutation
            outputDictionary['route_distance'] = shortestPermutationDistance
            outputDictionary['price_route'] = totalTravelCost
            outputDictionary['price_ingredients'] = totalCost-totalTravelCost
            outputDictionary['price_total'] = totalCost
            outputDictionary['shopping_list'] = shoppingList
            outputDictionary['coordinate_matrix'] = {}
            
            for location in coordinateMatrix:
                x = coordinateMatrix[location][0]
                y = coordinateMatrix[location][1]
                outputDictionary['coordinate_matrix'][location] = {'x': x, 'y': y}
            
            with open(wd + '/../frontEnd/BudgetBasket/app/assets/data.json', 'w') as file:
                file.write('data = ')
                json.dump(outputDictionary, file, indent=4, sort_keys=True)
                
        else:
            print("RouteType not programmed!")
            
        print('\n--------->Done\n\n\n')
            
def getInformation_bestPriceAtStore(priceMatrix, ingredientDictionary):
    bestPriceAtStore = 10000000 #set to a very large number so first price found is always best price
    completelyUnavailableIngredients = [] #elements in this list have both organic and non-organic versions unavailable in all stores
    substitutedIngredients = [] #elements in this list were originally unavailable, however their opposite ingredient (organic --> non-organic, non-organic --> organic) was available, then that new version was added to the storeWithBestPriceMatrix, so for example, if ingredient_137_organic is in the list, then ingredient_137_non-organic is the storeWithBestPriceMatrix, and ingredient_137_organic was what the user orginally requested
    storeWithBestPriceMatrix = {}
    
    for ingredient in ingredientDictionary:
        
        for store in priceMatrix: #checks all stores for originally selected ingredient
            if ingredient in priceMatrix[store].keys():
                if float(priceMatrix[store][ingredient]) < bestPriceAtStore: #currently doesnt have any added functionality if two stores just so happen to have the same price, this might be added in the future
                    bestPriceAtStore = priceMatrix[store][ingredient]
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
                        if float(priceMatrix[store][oppositeIngredient]) < bestPriceAtStore:
                            bestPriceAtStore = priceMatrix[store][oppositeIngredient]
                            storeWithBestPriceMatrix[oppositeIngredient] = store
                        else:
                            pass
        
        if ingredient not in storeWithBestPriceMatrix.keys() and oppositeIngredient not in storeWithBestPriceMatrix.keys():
            completelyUnavailableIngredients.append(ingredient)
        
        if oppositeIngredient in storeWithBestPriceMatrix.keys():
            substitutedIngredients.append(ingredient)
    
    return({'storeWithBestPriceMatrix': storeWithBestPriceMatrix, 'completelyUnavailableIngredients': completelyUnavailableIngredients, 'substitutedIngredients': substitutedIngredients})
    
def calculateRoute_bestPriceAtStore(coordinateMatrix, storeWithBestPriceMatrix): #this method generates one defined root to be the shortest where in all actuality for every route, there is an identical, reverse route. It is arbitrary which is selected. So if there are n routes generated, there are n/2 unique routes.
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

def getTotalPrice_bestPriceAtStore(storeWithBestPriceMatrix, priceMatrix, ingredientDictionary, totalTravelCost):
    #this operation removes the _non-organic and _organic tags from ingredients in the ingredientDictionary
    stripped_countDictionary = {}
    for ingredient in ingredientDictionary:
        temp = ingredient.split('_')[0] + '_' + ingredient.split('_')[1]
        stripped_countDictionary[temp] = ingredientDictionary[ingredient]
    
    #this operation removes the _non-organic and _organic tags from ingredients in the storeWithBestPriceMatrix
    stripped_storeDictionary = {}
    for ingredient in storeWithBestPriceMatrix:
        temp = ingredient.split('_')[0] + '_' + ingredient.split('_')[1]
        stripped_storeDictionary[temp] = storeWithBestPriceMatrix[ingredient]
    
    totalIngredientCost = 0.0
    for ingredient in storeWithBestPriceMatrix:
        ingredient_stripped = ingredient.split('_')[0] + '_' + ingredient.split('_')[1]
        totalIngredientCost += float(stripped_countDictionary[ingredient_stripped]) * float(priceMatrix[stripped_storeDictionary[ingredient_stripped]][ingredient])
    
    return(totalIngredientCost + totalTravelCost)

def getShoppingList(storeWithBestPriceMatrix, priceMatrix, ingredientDictionary):
    #this operation removes the _non-organic and _organic tags from ingredients in the ingredientDictionary
    stripped_countDictionary = {}
    for ingredient in ingredientDictionary:
        temp = ingredient.split('_')[0] + '_' + ingredient.split('_')[1]
        stripped_countDictionary[temp] = ingredientDictionary[ingredient]
    
    #this operation removes the _non-organic and _organic tags from ingredients in the storeWithBestPriceMatrix
    stripped_storeDictionary = {}
    for ingredient in storeWithBestPriceMatrix:
        temp = ingredient.split('_')[0] + '_' + ingredient.split('_')[1]
        stripped_storeDictionary[temp] = storeWithBestPriceMatrix[ingredient]
    
    shoppingDictionary = {}
    for ingredient in storeWithBestPriceMatrix:
        ingredient_stripped = ingredient.split('_')[0] + '_' + ingredient.split('_')[1]
        ingredient_count = stripped_countDictionary[ingredient_stripped]
        ingredient_store = stripped_storeDictionary[ingredient_stripped]
        
        #if ingredient_store not in shoppingDictionary.keys(): shoppingDictionary[ingredient_store] = []
        #shoppingDictionary[ingredient_store].append({'ingredient_name': ingredient, 'ingredient_count': ingredient_count})
        
        shoppingDictionary[ingredient] = {'ingredient_count': ingredient_count, 'ingredient_store': ingredient_store}
        
    return(shoppingDictionary)

def getDistance(pointA, pointB):
    distance = math.sqrt((float(pointB[0]) + float(pointA[0]))**2 + (float(pointB[1]) + float(pointA[1]))**2)
    
    return(distance)
    
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
