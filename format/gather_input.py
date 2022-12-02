def inputCompanies(resultsDict):
    isValid = False
    
    while isValid == False:
        companyList = inputCompaniesImpl(resultsDict)
        isValid = checkInput(companyList, resultsDict)
    return companyList

def inputCompaniesImpl(resultsDict):
    print('What companies do you want information on?') 
    for company in resultsDict.keys():
        print(company)
    print('\nEnter company names:')    
    companies = input()
    
    companies = companies.lower()
    # seperates companies into a list
    companyList = companies.split(", ") 
    if len(companyList) == 1:
        companyList = companies.split(",")
    if len(companyList) == 1:
        companyList = companies.split()
    return companyList

def checkInput(companyList, resultsDict):
    for company in companyList:
        if company not in resultsDict:
                print(f'{company} is not a valid company')
                return False
    return True

def enterSharePrice(companyDict, company):
    print(f"Enter current share price for {company}")
    sharePrice = input()
    companyDict[company].setSharePrice(sharePrice)
    return companyDict 

