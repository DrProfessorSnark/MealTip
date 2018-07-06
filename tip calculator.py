#Code for Tip Calculator

print('What is your bill total?')
bill=input() #Asks user to input bill total.
bill = float(bill) #Changes string into an float (Fixed whole number problem)
print('What percentage would you like to tip?')
tip = input()
tip = (float(tip)/100)
tip = bill * tip
tipTotal = round(tip, 2)
billTotal = bill + tipTotal
print('Your tip is: $',tipTotal)
print('Your total is: $',billTotal)

#print('Your total is:'
#Above prints tip amount and bill total.
