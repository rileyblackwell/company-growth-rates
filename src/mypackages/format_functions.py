def castToFloat(variable):
   notNum = True
   while notNum == True:
        try:
            variable = float(variable)
            notNum = False
        except:
            notValid = "\"{0}\" is not a number"
            notValid = notValid.format(variable)
            print(notValid)
            print("Enter a number")
            variable = input()
   return variable 

def enterSharePrice(companyDict, resultsDict, companyName):
    enterPrice = "Enter current share price for {0}"
    enterPrice = enterPrice.format(companyName)
    print(enterPrice)
    sharePrice = input()
    companyDict[companyName].setSharePrice(sharePrice)
    return companyDict

def formatGrowthRate(data):
    data *= 100
    data -= 100
    data = round(data,2)
    data = str(data)
    data += "%"
    return data

def formatOpMargin(data):
    data *=100
    data = round(data,2)
    data = str(data)
    data += "%"
    return data

def formatEPS(data):
    data -= 1
    data *= 100
    data = round(data,2)
    data = str(data)
    data += "%"
    if data[0] == "-":
        data = data[1:]
        data += " buyback"
    else:
        data += " share increase"
    return data