def castToFloat(num):
   notNum = True
   while notNum == True:
        try:
            num = float(num)
            notNum = False
        except:
            print(f"\"{num}\" is not a number\nEnter a number")
            num = input()
   return num 

def formatGrowthRate(data):
    data *= 100
    data -= 100
    data = round(data, 2)
    data = str(data)
    data += "%"
    return data

def formatOpMargin(data):
    data *=100
    data = round(data, 2)
    data = str(data)
    data += "%"
    return data

def formatEPS(data):
    data -= 1
    data *= 100
    data = round(data, 2)
    data = str(data)
    data += "%"
    if data[0] == "-":
        data = data[1:]
        data += " buyback"
    else:
        data += " share increase"
    return data

def formatResults(resultsDict, company, key):
    totalResults = ''
    if key == 'revenue':
        results = resultsDict[company].getRevenue()
    elif key == 'opinc':
        results = resultsDict[company].getOperatingIncome()
    elif key == 'eps':
        results = resultsDict[company].getEPS()
    elif key == 'pe':
        results = resultsDict[company].getPE()

    for result in results:
        totalResults += (str(result) + " " )
    return totalResults    