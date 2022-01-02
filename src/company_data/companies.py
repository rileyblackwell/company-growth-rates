import pandas as pd

class Company(object):
    def __init__(self, r, g, m, omg, mom, s, sc):
        self.revenue = r
        self.growthRate = g
        self.opMargin = m
        self.opMarginGrowthRate = omg
        self.maxOpMargin = mom
        self.shares = s
        self.sharePrice = 0
        self.shareChange = sc
        self.years = 10 
         
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