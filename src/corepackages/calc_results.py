from corepackages.classes import Results
from formatpackages.format_functions import castToFloat

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
    
    resultsObj = Results()
    resultsObj.setRevenue(values)
    resultsDict[companyName] = resultsObj
    return resultsDict

def calcOpInc(companyDict, resultsDict, companyName):
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

def calcEPS(companyDict, resultsDict, companyName):
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

def calcPE(companyDict, resultsDict, companyName):
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
