
import time

def smokingStats():
    print('')
    qYears = input('How many years did you smoke? ')
    print('')
    qCigsPerDay = input('About how many per day did you smoke over that time? (There are 20 in a pack) ')
    print('')
    giveAway = input('You know you let people bum them... About how many do you think for every pack? ')
    print('')
    savingItem = input('been saving up for anything? What? ')
    print('')
    savingCost = input('how much does a ' + savingItem + ' cost? ')
    
    totalCigs = int(qCigsPerDay) * (float(qYears) * 365)
    totalPacks =  round(totalCigs / 20)
    moneyWasted = round(totalPacks * 5.63, 2)
    hoursWasted = (totalCigs * 6) / 60
    daysWasted = round(int(hoursWasted) / 24, 1)    
    moneyToFriendsPerPack = round((float(giveAway) * int(totalPacks)) / 20 * 5.63, 2)
    moneyWastedBeforeBums = round(moneyWasted - moneyToFriendsPerPack, 2)
    cigsGivenOut = round(float(giveAway) * float(totalPacks))
    yourTotalCigs = int(totalCigs) - int(cigsGivenOut)
    totalEnhales = int(yourTotalCigs) * 11
    yearsWasted = round(int(daysWasted) / 365, 2)
    itemsWithSavings = round(float(moneyWasted) / float(savingCost), 1)
    oneBigCigFeet = round(float(yourTotalCigs) * 3.25 / 12, 2)
    oneBigCigMiles = round(float(oneBigCigFeet) / 5280, 2)
    
    aMoneyWasted = str(moneyWasted)
    aTotalPacks = str(totalPacks)
    aTotalCigs = str(totalCigs)
    aTotalEnhales = str(totalEnhales)
    aHoursWasted = str(hoursWasted)
    aDaysWasted = str(daysWasted)
    aMoneyToFriendsPerPack = str(moneyToFriendsPerPack)
    aMoneyWastedBeforeBums = str(moneyWastedBeforeBums)
    aCigsGivenOut = str(cigsGivenOut)
    aYourTotalCigs = str(yourTotalCigs)
    aYearsWasted = str(yearsWasted)
    aItemsWithSavings = str(itemsWithSavings)
    aOneBigCigFeet = str(oneBigCigFeet)
    aOneBigCigMiles = str(oneBigCigMiles)

    time.sleep(1.0)
    print('')
    print('====================================================')
    print('')
    print('You have SPENT $' + aMoneyWasted + ' on cigarettes')
    print('Would have only been $' + aMoneyWastedBeforeBums + ', which still sucks')
    print('BUT it was $' + aMoneyToFriendsPerPack + ' MORE because you were nice and shared')
    print('')
    print('You have BOUGHT ' + aTotalPacks + ' packs')
    print('')
    print('You have SMOKED ' + aYourTotalCigs + ' cigarettes and have given away another ' + aCigsGivenOut)
    print('')
    print('You have SMOKED ' + aOneBigCigMiles + ' miles worth of cigarettes')
    print('')
    print('You have taken ' + aTotalEnhales + ' PUFFS')
    print('')
    print('You have SPENT ' + aHoursWasted + ' HOURS of your life smoking')
    print('Thats ' + aDaysWasted + ' DAYS worth of time wasted...')
    if float(aDaysWasted) >= 365:
        print('Or ' + aYearsWasted + ' YEARS...')
    else:
        exit
    print('')
    print('Oh, and you could have already bought ' + aItemsWithSavings + ' ' + savingItem + 's and had money left over!')
    print('')
    print('====================================================')
    print('')
    exit
    
print('Are you, or have you ever been, a smoker?')
print('')
smoker = input('yes or no? ')

if smoker == 'no':
    print('Good! Complete waste of time!')

elif smoker == 'yes':
    smokingStats()










    
