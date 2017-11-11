# CTI- 110
# M5HW3- Factorial
# Laura Saunders
# 10/21/2017

def main():
    # This program will ask the user for a nonnegative integer and use it to calculate the factorial of that number.

    integer = int( input("Enter a nonnegative integer? "))

    factorial = 1
    
    for number in range(1, integer + 1):
        factorial = factorial * number

    print( "The factorial of", integer, "is", factorial )

main()
