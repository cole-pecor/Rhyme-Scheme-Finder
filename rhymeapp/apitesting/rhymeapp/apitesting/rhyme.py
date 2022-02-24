# '''
# Created on Jan 31, 2022
#
# @author: Cole Pecor
# '''
#

import requests
import json
from pip._vendor.urllib3 import response
from pickle import FALSE

stringInput = input("Type string: ")
# userInput = input("Type word: ")

def removePunc(input):
    punctuation= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    emptyString=""
    for x in punctuation:
        input=input.replace(x,emptyString)
    return input.lower()

listString = removePunc(stringInput).split()
ultimateList = []
ultimateString = ""
rhymeDictionary = {}

def findRhyme(input):
        # Finds perfect rhymes
        response = requests.get("https://api.datamuse.com/words?rel_rhy=" + input)
        text = response.text
        parsed = json.loads(text)

        
        i = 0
        rhymes = []
        str1 = ""

        for x in parsed:
            # print(parsed[iteration]['word'])
            rhymes.append(parsed[i]['word'])
            str1 += parsed[i]['word'] + " " #maybe move space
            i += 1
    
        i = 0
        
        findRhyme.list = rhymes
        findRhyme.str = str1  


def findIntersection(list):

    i = 0
    w1List = []
    w2List = []
    first_key = False
    
    for x in range(len(list)):
        # print(list[i])
        
        # Setting i to x avoids reiterating previous pairings
        i = x
        
        findRhyme(list[x])
        w1List = findRhyme.list
        
        for w in range(len(list)):
            # Avoids asking for out of range index
            if (i) < (len(list) - 1):
                
                inDict = True
                
                findRhyme(list[i + 1])
                w2List = findRhyme.list
                
                # print(*w1List)
                # print(*w2List) 
                # print(set(w1List).intersection( set(w2List) ))
                
                if set(w1List).intersection( set(w2List) ):
                    # Debug printing
                    # print("There is a rhyme between " + list[x] + " and " + list[i+1])
                    
                    if not (list[x] == list[i+1]):
                    
                        # Create dictionary value including all the rhymes with a given word
                        if list[x] in rhymeDictionary.keys():
                            rhymeDictionary[list[x]].append(i+1)
                        else:
                            if first_key == False:
                                rhymeDictionary[list[x]] = [x]
                                rhymeDictionary[list[x]].append(i+1)
                                first_key = True
                            else:
                                for key in rhymeDictionary:
                                    if x not in rhymeDictionary[key]:
                                        inDict = False
                                    else:
                                        inDict = True
                                if inDict == False:
                                    rhymeDictionary[list[x]] = [x]
                                    rhymeDictionary[list[x]].append(i+1)                                    
                # else:
                #     print("")
                
            i +=1  
        
    # print("FINISHED")
    print(rhymeDictionary)

findIntersection(listString)