import pandas as pd

class Company(object):
    def __init__(self, companyName, revenue, growth_rate, op_margin, op_margin_growth_rate, 
                 max_op_margin, shares, share_change):
        self.companyName = companyName
        self.revenue = revenue
        self.growthRate = growth_rate
        self.opMargin = op_margin
        self.opMarginGrowthRate = op_margin_growth_rate
        self.maxOpMargin = max_op_margin
        self.shares = shares
        self.sharePrice = 0
        self.shareChange = share_change
        self.years = 10 # view 10 years by deafult

    def getCompanyName(self):
        return self.companyName      
    def getRevenue(self):
        return self.revenue
    def getGrowthRate(self):
        return self.growthRate
    def getOpMargin(self):
        return self.opMargin
    def getOpMarginGrowthRate(self):
        return self.opMarginGrowthRate
    def getMaxOpMargin(self):
        return self.maxOpMargin
    def getShares(self):
        return self.shares
    def getShareChange(self):
        return self.shareChange
    def getSharePrice(self):
        return self.sharePrice
    def getYears(self):
        return self.years
    
    def setRevenue(self, newValue):
        self.revenue = newValue
    def setGrowthRate(self, newRate):
        self.growthRate = newRate
    def setOpMargin(self, newMargin):
        self.opMargin = newMargin
    def setOpMarginGrowthRate(self, newMarginGrowth):
        self.opMarginGrowthRate = newMarginGrowth
    def setShareChange(self, newShareChange):
        self.shareChange = newShareChange
    def setSharePrice(self, sp):
        self.sharePrice = sp
    def setYears(self, y):
        self.years = y

def createCompanyDict():    
    """
        EFFECTS: Returns a dictionary- key: company name, value: a Company object 
        Note: Make sure that all data that is read in is a number! Column names are all lowercase!
    """
    companyDict = {}
    companyDataFrame = pd.read_csv("CompanyData.csv") 
    
    for companyName in companyDataFrame:
        companyObj = Company(
            companyName, companyDataFrame.loc[0,companyName], companyDataFrame.loc[1,companyName],
            companyDataFrame.loc[2,companyName], companyDataFrame.loc[3,companyName], 
            companyDataFrame.loc[4,companyName], companyDataFrame.loc[5,companyName],
            companyDataFrame.loc[6,companyName]) 
        companyDict[companyName] = companyObj
    return companyDict        