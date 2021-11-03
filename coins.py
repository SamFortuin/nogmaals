# name of student: Sam Fortuin
# number of student: 99059050
# purpose of program: Change Calculator
# function of program: turns value into an amount of coins
# structure of program: while loop

toPay = int(float(input('Amount to pay: '))* 100) #turns input into float in case of cents, multiplies by 100 to make a valid int
paid = int(float(input('Paid amount: ')) * 100) #turns input into float in case of cents, multiplies by 100 to make a valid int
change = paid - toPay #

if change > 0: #checks if any change is even needed
  coinValue = 500 #sets starting coin value, in this case €5
  
  while change > 0 and coinValue > 0: #checks if there is any coin value and change left to pay
    nrCoins = change // coinValue #floor devision to return maximum possible integer

    if nrCoins > 0: #prints the max amount of coins possible with current coin value
      print('return maximal', nrCoins, 'coins of', coinValue, 'cents!') #prints text to tell the user which coinvalue they're at and the max amount of coins being able to be payed out with that value
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #asks user for input, converts it to an int, and stores it to be used in change
      change -= nrCoinsReturned * coinValue #change = change - (nrCoinsReturned * coinValue), change is recalculated to see if while is still true

# comment on code below: decreases coin value in set steps for nrCoins
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #if any cahnge was not able to be payed because of coin incompat prints leftover amount, prints done when change was able to be payed in full
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')