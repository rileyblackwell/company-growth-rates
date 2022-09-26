from format.format_functions import castToFloat 

class Results(object):
    def __init__(self, noValue = ["No values for this instance"]):
        self.revenue = noValue 
        self.operatingIncome = noValue 
        self.eps = noValue
        self.pe = noValue
    
    def getRevenue(self):
        return self.revenue
    def getOperatingIncome(self):
        return self.operatingIncome      
    def getEPS(self): 
        return self.eps
    def getPE(self):
        return self.pe
    
    def setRevenue(self, r):
        self.revenue = r
    def setOperatingIncome(self, o):
        self.operatingIncome = o
    def setEPS(self, e):
        self.eps = e
    def setPE(self, p):
        self.pe = p


def calcRevenue(companyDict, resultsDict, companyName):
    values = []
    values.append(companyDict[companyName].getRevenue())
    revenue = companyDict[companyName].getRevenue()
    growthRate = companyDict[companyName].getGrowthRate()
    years = companyDict[companyName].getYears()
    n = 0
    
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
    margin = companyDict[companyName].getOpMargin()
    growthRate = companyDict[companyName].getOpMarginGrowthRate()
    margin = (growthRate * -1) + margin
    maxMargin = companyDict[companyName].getMaxOpMargin()
    years = companyDict[companyName].getYears()
    revenueList = resultsDict[companyName].getRevenue() 
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
    shares = companyDict[companyName].getShares() 
    shareChange = companyDict[companyName].getShareChange()
    epsList = []

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
            pe = round(pe, 2)
            peList.append(pe)
            
        resultsDict[companyName].setPE(peList)
    return resultsDict


def createResultsDict(companyDict):
    companyKeys = companyDict.keys()
    resultsDict = {}
    
    for companyName in companyKeys: 
        resultsDict = calcRevenue(companyDict, resultsDict, companyName)
        resultsDict = calcOpInc(companyDict, resultsDict, companyName)
        resultDict = calcEPS(companyDict, resultsDict, companyName)
    return resultsDict        