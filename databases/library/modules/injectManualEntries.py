#!/usr/bin/env python

import os
import random

def __main__(wd, manualIngredientsList, manualRecipesList, availableIngredientsList, recipesList, priceVariance, organicPriceMultiplier, chanceToBeOrganic):
    os.chdir(wd + '/library/data')
    
    manualIngredients = parseManualIngredients(manualIngredientsList)
    manualRecipes = parseManualRecipes(manualRecipesList)
    
    storeDirectory = os.listdir(os.getcwd())
    numStores = 0
    for item in storeDirectory:
        if item.startswith("store"):
            numStores += 1
        else:
            pass
        
    for i in range(0, numStores):
        with open('store' + str(i) + '.store', 'a') as chunk:
            for ingredient in manualIngredients:
                minPrice = float(manualIngredients[ingredient])*(float(100 - priceVariance)/100.00)
                maxPrice = float(manualIngredients[ingredient])*(float(100 + priceVariance)/100.00)
                randomPrice = float(random.randint(int(minPrice*1000), int(maxPrice*1000))/1000.00)
                
                chunk.write(ingredient + '\t' + str(randomPrice) + '\t' + 'non-organic' + '\n')
                
                '''
                if (random.randint(1,100) <= chanceToBeOrganic):
                    chunk.write(ingredient + '\t' + str(randomPrice * float(organicPriceMultiplier)) + '\t' + 'organic' + '\n')
                '''
                
        chunk.close()
    
    with open(availableIngredientsList, 'a') as chunk:
        for ingredient in manualIngredients:
            chunk.write(ingredient + '\t' + manualIngredients[ingredient] + '\t' + 'null' + '\n')
            
    chunk.close()
    
    with open(recipesList, 'a') as chunk:
        for recipe in manualRecipes:
            chunk.write(recipe)
            for ingredient in manualRecipes[recipe]:
                chunk.write('\t' + ingredient)
                
            chunk.write('\n')
                
    chunk.close()
                
                
def parseManualIngredients(manualIngredientsList):
    manualIngredients = {}
    with open(manualIngredientsList) as chunk:
        for line in chunk:
            manualIngredients[line.strip().split('=')[0]] = line.strip().split('=')[1]
    
    chunk.close()
    
    return(manualIngredients)
    
def parseManualRecipes(manualRecipesList):
    manualRecipes = {}
    with open(manualRecipesList) as chunk:
        for line in chunk:
            manualRecipes[line.strip().split('=')[0]] = line.strip().split('=')[1].split(',')
            
    chunk.close()
    
    return(manualRecipes)