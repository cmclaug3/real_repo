#for the 2016 tax year
#still need to auto complete list(s) of taxRun() for MatPlotLib

import matplotlib as mpl

def taxRun():
    
    salary = 10000
    while salary <= 300000:
    
        if salary <= 9275:
            netSal = salary * 0.9

        elif salary > 9275 and salary <= 37650:
            netSal = salary - 927.50 - ((salary - 9275) * .15)

        elif salary > 37651 and salary <= 91150:
            netSal = salary - 5183.75 - ((salary - 37650) * .25)

        elif salary > 91151 and salary <= 190150:
            netSal = salary - 18558.75 - ((salary - 91150) * .28)

        elif salary > 190151 and salary <= 413350:
            netSal = salary - 46278.75 - ((salary - 190150) * .33)

        elif salary > 413351 and salary <= 415050:
            netSal = salary - 119934.75 - ((salary - 413350) * .35)

        elif salary > 415051:
            netSal = salary - 120529.75 - ((salary - 415050) * .396)

        percentTax = round(100 - (netSal / salary) * 100, 2)
        taxMoney = salary - netSal
        print('$',salary,' make $',netSal,' at %',percentTax,' you pay $',taxMoney)
        print('')
        salary += 5000
        

def taxQ(salary):

    if salary <= 9275:
        netSal = salary * 0.9

    elif salary > 9275 and salary <= 37650:
        netSal = salary - 927.50 - ((salary - 9275) * .15)

    elif salary > 37651 and salary <= 91150:
        netSal = salary - 5183.75 - ((salary - 37650) * .25)

    elif salary > 91151 and salary <= 190150:
        netSal = salary - 18558.75 - ((salary - 91150) * .28)

    elif salary > 190151 and salary <= 413350:
        netSal = salary - 46278.75 - ((salary - 190150) * .33)

    elif salary > 413351 and salary <= 415050:
        netSal = salary - 119934.75 - ((salary - 413350) * .35)

    elif salary > 415051:
        netSal = salary - 120529.75 - ((salary - 415050) * .396)

    percentTax = round(100 - (netSal / salary) * 100, 2)
    taxMoney = salary - netSal
    print('$',salary,' make $',netSal,' at %',percentTax,' you pay $',taxMoney)


#MatPlotLib graph to show testing

# X axis (salary)
def taxPlotX(xSalLow,xSalHigh,interval):
    xSalaryList = list(range(xSalLow,xSalHigh,interval))
    print(xSalaryList)
    
#    yPercentTaxList = 



# Y axis (netSal? or percentTax?)

    
        

    


    
    
                        
    

                                      

                                      
        
        
        
