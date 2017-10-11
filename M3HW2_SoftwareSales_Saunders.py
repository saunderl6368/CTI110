# CTI 110
# M3HW2- Software Sales
# Laura Saunders
# 9/24/2017

def main():
     #This program will compute the discount and total price depending on the number of packages purchased.

# A software company sells a package that retails for $99.  Discounts are given for volume purchases as follows:
# Quantity 10-19 is 10% discount
# Quantity 20-49 is 20% discount
# Quantity 50-99 is 30% discount
# Quantity 100+ is 40% discount


     numberOfPackages = int (input ("Enter the number of packages purchased: "))

     packagePrice = 99

     if numberOfPackages < 10:
         discount = 0
     elif numberOfPackages < 20:
         discount = 0.10
     elif numberOfPackages < 50:
         discount = 0.20
     elif numberOfPackages <100:
         discount = 0.30
     elif numberOfPackages >= 100:
         discount = 0.40

     subTotal = numberOfPackages * packagePrice
     amountOfDiscount = discount * subTotal
     total = subTotal - amountOfDiscount

     print ("Amount of Discount: $" + format (amountOfDiscount, ",.2f"))
     print ("Total Amount of Purchase Including Discount: $" + format (total, ",.2f"))
main()



