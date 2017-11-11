# CTI- 110
# M5HW2- Running Total
# Laura Saunders
# 10/21/2017

def main():
    # Write a program that asks the user to enter a series of numbers.

# Initialize the accumulator.
    total = 0

    number = float( input("Enter a number? "))

    while number > -1:
        total = total + number
        number = float( input("Enter a number? "))

    print("Total:", total)

main()
