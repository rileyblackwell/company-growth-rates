from mypackages.classes import company, results
from mypackages.format_functions import castToFloat, formatGrowthRate, formatOpMargin, formatEPS
from mypackages.gather_input import inputCompanies, enterSharePrice
import pandas as pd



def createCompanyDict():    
    """
        Make sure that all read data is a number! Column names are all lowercase!
    """
    companyDict = {}
    companyDataDF = pd.read_csv("CompanyDataCSV.txt") 
    for companyName in companyDataDF:
        companyObj = company(
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
        resultsDict = calcOperatingIncome(companyDict, resultsDict, companyName)
        resultDict = EPS(companyDict, resultsDict, companyName)
    return resultsDict

def calcRevenue(companyDict, resultsDict, companyName):
    values = []
    values.append(companyDict[companyName].getRevenue())
    n = 0
    years = companyDict[companyName].getYears()
    revenue = companyDict[companyName].getRevenue()
    growthRate = companyDict[companyName].getGrowthRate()
    
    while n < years:
        revenue *= growthRate
        revenue = round(revenue,2)
        values.append(revenue)
        n += 1
    
    resultsObj = results()
    resultsObj.setRevenue(values)
    resultsDict[companyName] = resultsObj
    return resultsDict

def calcOperatingIncome(companyDict, resultsDict, companyName):
    revenueList = resultsDict[companyName].getRevenue()     
    margin = companyDict[companyName].getOpMargin()
    growthRate = companyDict[companyName].getOpMarginGrowthRate()
    margin = (growthRate * -1) + margin
    maxMargin = companyDict[companyName].getMaxOpMargin()
    years = companyDict[companyName].getYears()
    result = []
    
    for revenue in revenueList:
        margin += growthRate    
        if margin > maxMargin:
            margin = maxMargin
        value = margin * revenue
        value = round(value,2)
        result.append(value)
    
    resultsDict[companyName].setOperatingIncome(result)
    return resultsDict

def EPS(companyDict, resultsDict, companyName):
    operatingIncome = resultsDict[companyName].getOperatingIncome()
    epsList = []
    n = 0
    shares = companyDict[companyName].getShares() 
    shareChange = companyDict[companyName].getShareChange()
    
    for year in operatingIncome:
        shares *= shareChange
        earnedPerShare =  (year * 1000000000 *.95) / shares
        earnedPerShare = round(earnedPerShare,2)
        epsList.append(earnedPerShare)
        
    resultsDict[companyName].setEPS(epsList)
    return resultsDict

def PE(companyDict, resultsDict, companyName):
    sharePrice = companyDict[companyName].getSharePrice()
    if sharePrice != "skip":
        sharePrice = castToFloat(sharePrice)
        epsList = resultsDict[companyName].getEPS()
        peList = []
        
        for eps in epsList:
            pe = sharePrice / eps
            pe = round(pe,2)
            peList.append(pe)
            
        resultsDict[companyName].setPE(peList)
    return resultsDict



def viewCompanies(resultsDict, companyDict, companyNamesList):
    for companyName in companyNamesList:
        growthRate = companyDict[companyName].getGrowthRate()
        growthRate = formatGrowthRate(growthRate)
        opMargin = companyDict[companyName].getOpMargin()        
        opMargin = formatOpMargin(opMargin)
        shareChange = companyDict[companyName].getShareChange()
        shareChange = formatEPS(shareChange)
        maxMargin = companyDict[companyName].getMaxOpMargin()
        maxMargin = formatOpMargin(maxMargin)
        marginGrowth = companyDict[companyName].getOpMarginGrowthRate()
        marginGrowth = formatOpMargin(marginGrowth)
        marginGrowth = marginGrowth[:-1]
        marginGrowth += " basis points"
        companyDict = enterSharePrice(companyDict, resultsDict, companyName)
        resultsDict = PE(companyDict, resultsDict, companyName)

        print("\n", companyName.upper())
        print("Revenue --> " + "growth rate: " + growthRate, resultsDict[companyName].getRevenue())
        print("Operating Income --> "  + "margin: " + opMargin + " max " + maxMargin, resultsDict[companyName].getOperatingIncome(),  " growth: " + marginGrowth )
        print("EPS --> " + shareChange, resultsDict[companyName].getEPS())
        print("PE --> ", resultsDict[companyName].getPE())

def viewAnotherModel(companyDict, resultsDict):
    companyNamesList = inputCompanies(resultsDict)
    print("Modify revenue growth, op margin, or share change? Select all catagories that apply or type \"none\".")
    newParameters = input() 
    newParameters = newParameters.lower()
    newParametersList = newParameters.split(", ")
     
    for companyName in companyNamesList:
        for i in newParametersList:
            if i in "revenue growth":
                enterGrowth = "Enter a new revenue growth rate for {0} ex. 1.25 (25%)"
                enterGrowth = enterGrowth.format(companyName)
                print(enterGrowth)
                newGrowthRate = input()
                newGrowthRate = castToFloat(newGrowthRate)
                companyDict[companyName].setGrowthRate(newGrowthRate)
            elif i in "op margin":
                enterMargin = "Enter a new starting operating margin for {0} ex. 0.25 (25%)"
                enterMargin = enterMargin.format(companyName)
                print(enterMargin)
                newMargin = input()
                newMargin = castToFloat(newMargin)
                companyDict[companyName].setOpMargin(newMargin)
                enterMarginGrowth = "Enter a new growth rate for operating margin (basis points) current: {0} ({1} pts)  or type \"same\""
                currentRate = companyDict[companyName].getOpMarginGrowthRate()
                currentPoints = currentRate * 100
                enterMarginGrowth = enterMarginGrowth.format(currentRate,currentPoints)
                print(enterMarginGrowth)
                newMarginGrowth = input()
                if newMarginGrowth not in "same":
                    newMarginGrowth = castToFloat(newMarginGrowth)
                    companyDict[companyName].setOpMarginGrowthRate(newMarginGrowth)   
            elif i in "share change":
                enterShares = "Enter a new rate for change in share count for {0} ex. 0.95 (5% buyback) or 1.05 (5% increase)"
                enterShares = enterShares.format(companyName)
                print(enterShares)
                newShareCount = input()
                newShareCount = castToFloat(newShareCount)
                companyDict[companyName].setShareChange(newShareCount)
    resultsDict = createResultsDict(companyDict)
    viewCompanies(resultsDict,companyDict,companyNamesList)

def answerViewAnother(answer):
    if len(answer) == 3:
        try:
            answer.index("yes")
        except ValueError:
            return False
    elif len(answer) == 1:
        try:
            answer.index("y")
        except ValueError:
            return False
    else:
        return False
    
    return True

companyDict = createCompanyDict()
resultsDict = createResultsDict(companyDict)
companyNamesList = inputCompanies(resultsDict)
viewCompanies(resultsDict,companyDict,companyNamesList)
print()
print("Do you want to view another model Y or N?")
answer = input()
answer = answer.lower()
viewModel = answerViewAnother(answer)
while viewModel:
    viewAnotherModel(companyDict, resultsDict)
    print()
    print("Do you want to view another model Y or N?")
    answer = input()
    answer = answer.lower()
    viewModel = answerViewAnother(answer)