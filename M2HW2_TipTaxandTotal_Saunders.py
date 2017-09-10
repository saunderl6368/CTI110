#CTI-110
#M2HW2- Tip Tax Total
#Laura Saunders
#9/10/2017
foodCost = float(input ("Enter the charge for the food: "))
print ("The cost of the food is $", format (foodCost, ",.2f"))
salesTax = foodCost * 0.07
#Display the amount of sales tax which is at a rate of 7%.
print ("The sales tax is $", format (salesTax, ",.2f"))
tipAmount = foodCost * 0.18
#Display the amount of the tip at 18% of the food cost.
print ("The tip amount is $", format (tipAmount, ",.2f"))
totalCost = foodCost + salesTax + tipAmount
#Display the Total Cost.
print ("The total cost of the meal with the tip and tax included is $", format (totalCost, ",.2f"))

