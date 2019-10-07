


#This Method will read in Song Files.
#This Method will only recieve song files that
#are known to be a specific language
#as this will be the training set.
#Read in languages from txt file



#Possible way of storing Data
#Through numpy array.
#.npy array
import numpy as np


def training(data,Language):
    f = open("Language.txt","r")
    f1 = f.readlines()
    x = f1.split(",")
    f.close()
    #Change Later
    specifiedFile = "specifiedLocationOfTextFile"
    if language in x:
        #Train Data


        print("train Data")
    elif:
        f = open("Language.txt","w")
        f.write(","+Language)
        f.close()
        #Create Dataset
        np.save(specifiedFile,data)
