45#Takes an amount from the user and calculates the tip for the given amount in 15% and 20%
#requires amount input twice.
#Maciej Sudol

print ('What was the amount of the bill')
bill = input()
bill2 = input()
bill = int(bill)
bill2 = int(bill2)
tip = 0.15
tip2 = 0.20
bill = bill * tip
bill2 = bill2 * tip2
print ('The tip for 15% is: ',bill)
print ('The tip for 20% is: ',bill2)

