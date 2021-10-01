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