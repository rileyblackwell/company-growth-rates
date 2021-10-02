import pandas as pd
from corepackages.classes import Company
from corepackages.calc_results import calcRevenue, calcOpInc, calcEPS

def createCompanyDict():    
    """
        Make sure that all read data is a number! Column names are all lowercase!
    """
    companyDict = {}
    companyDataDF = pd.read_csv("CompanyDataCSV.txt") 
    for companyName in companyDataDF:
        companyObj = Company(
            companyDataDF.loc[0,companyName],companyDataDF.loc[1,companyName],
            companyDataDF.loc[2,companyName],companyDataDF.loc[3,companyName], 
            companyDataDF.loc[4,companyName],companyDataDF.loc[5,companyName],
            companyDataDF.loc[6,companyName]) 
        companyDict[companyName] = companyObj
    return companyDict

def createResultsDict(companyDict):
    companyKeys = companyDict.keys()
    resultsDict = {}
    for companyName in companyKeys: 
        resultsDict = calcRevenue(companyDict, resultsDict, companyName)
        resultsDict = calcOpInc(companyDict, resultsDict, companyName)
        resultDict = calcEPS(companyDict, resultsDict, companyName)
    return resultsDict