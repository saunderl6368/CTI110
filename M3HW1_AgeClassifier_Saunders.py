# CTI-110
# M3HW1- Age Classifier
# Laura Saunders
# 9/24/17

def main():
    #This program will classify a person's age.
    
    
# If the person is 1 year old or less, he or she is an infant.
# If the person is older than one year, but younger than 13 years, he or she is a child.
# If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
# If the person is at least 20 years old, he or she is an adult.

    userAge = int( input( "Enter the person's age: "))

    if userAge <= 1:
        print ("The person is an infant.")
    elif userAge < 13:
        print ("The person is a child.")
    elif userAge < 20:
        print ("The person is a teenager.")
    elif userAge >= 20:
        print ("The person is an adult.")

main()

