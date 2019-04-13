#!/usr/bin/env python

import os

def __main__(wd):
    coordinateMatrix = {}
    storeDirectory = os.listdir(wd + '/../databases/library/data/')
    numStores = 0
    
    for item in storeDirectory:
        if item.startswith("store"):
            numStores += 1
        else:
            pass
            
    for i in range(0,numStores):
        coordinateMatrix['store_' + str(i)] = getStoreCoordinates(wd + '/../databases/library/data/store' + str(i) + '.store')

    return(coordinateMatrix)

def getStoreCoordinates(store):
    with open(store, 'r') as chunk:
        coordinates = []
        for line in chunk:
            if line.startswith("#store"):
                coordinates = line.strip().split('\t')[1].strip(')').strip('(').split(',')
            else:
                pass
            
    chunk.close()
    
    return(coordinates)