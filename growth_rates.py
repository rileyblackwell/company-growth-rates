from format.format_functions import *
from format.gather_input import inputCompanies, enterSharePrice
from company_data.companies import createCompanyDict
from results_data.results import createResultsDict, calcPE


def viewCompanies(resultsDict, companyDict, companyList):
    for company in companyList:
        growthRate = formatGrowthRate(companyDict[company].getGrowthRate())   
        opMargin = formatOpMargin(companyDict[company].getOpMargin())
        shareChange = formatEPS(companyDict[company].getShareChange())
        maxMargin = formatOpMargin(companyDict[company].getMaxOpMargin())
        marginGrowth = formatOpMargin(companyDict[company].getOpMarginGrowthRate())
        marginGrowth = marginGrowth[:-1]
        marginGrowth += " basis points"
        companyDict = enterSharePrice(companyDict, company)
        resultsDict = calcPE(companyDict, resultsDict, company)
         
        print("\n", company.upper())
        print(f"Revenue --> growth rate: {growthRate}  " + formatResults(resultsDict, company, 'revenue'))
        print(f"Operating Income --> margin: {opMargin} max: {maxMargin}, growth: {marginGrowth}  " + formatResults(resultsDict, company, 'opinc'))
        print(f"EPS --> {shareChange}  " + formatResults(resultsDict, company, 'eps'))
        print("PE -->  " + formatResults(resultsDict, company, 'pe') + "\n")

def viewAnotherModel(companyDict, resultsDict):
    companyList = inputCompanies(resultsDict)
    
    print("Modify revenue growth, op margin, or share change? Select all catagories that apply or type \"none\".")
    newParameters = input() 
    newParameters = newParameters.lower()
    parametersList = newParameters.split(", ")
     
    for company in companyList:
        for parameter in parametersList:
            if parameter in "revenue growth":
                print(f"Enter a new revenue growth rate for {company} ex. 1.25 (25%)")
                newGrowthRate = input()
                newGrowthRate = castToFloat(newGrowthRate)
                companyDict[company].setGrowthRate(newGrowthRate)
            
            elif parameter in "op margin":
                print(f"Enter a new starting operating margin for {company} ex. 0.25 (25%)")
                newMargin = input()
                newMargin = castToFloat(newMargin)
                companyDict[company].setOpMargin(newMargin)
                currentRate = companyDict[company].getOpMarginGrowthRate()
                currentPoints = currentRate * 100
                print(f"Enter a new growth rate for operating margin (basis points) current: {currentRate} ({currentPoints} pts)  or type \"same\"")
                newMarginGrowth = input()
                if newMarginGrowth not in "same":
                    newMarginGrowth = castToFloat(newMarginGrowth)
                    companyDict[company].setOpMarginGrowthRate(newMarginGrowth)   
            
            elif parameter in "share change":
                print(f"Enter a new rate for change in share count for {company} ex. 0.95 (5% buyback) or 1.05 (5% increase)")
                newShareCount = input()
                newShareCount = castToFloat(newShareCount)
                companyDict[company].setShareChange(newShareCount)
    
    resultsDict = createResultsDict(companyDict)
    viewCompanies(resultsDict, companyDict, companyList)

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
companyList = inputCompanies(resultsDict)

viewCompanies(resultsDict, companyDict, companyList)

print("\nDo you want to view another model Y or N?")
answer = input()
viewModel = answerViewAnother(answer.lower())

while viewModel == True:
    viewAnotherModel(companyDict, resultsDict)
    print("\nDo you want to view another model Y or N?")
    answer = input()
    viewModel = answerViewAnother(answer.lower())
 
    