#CTI- 110
#M5T2- Bug Collector
#Laura Saunders
#10/21/2017

def main():
    #Program will display total number of bugs collected.

    # Initialize the accumulator.
    total = 0
    # Get the bugs collected for each day.
    for day in range(1, 8):
        # Prompt user for number of bugs.
        print("Enter the bugs collected on day", day)

        # Input number of bugs.
        bugs = int(input())

        # Add bugs to total.
        total = total + bugs
    
    # Display the total bugs.
    print("You collected a total of", total, "bugs.")

main()

    
