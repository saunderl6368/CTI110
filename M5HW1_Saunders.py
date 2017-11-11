# CTI- 110
# M5HW1- Distance Traveled
# Laura Saunders
# 10/21/2017

def main():
    #Program will display hours and distance traveled.

# distance = speed * time

    speed = float( input("What is the speed of the vehicle in mph? "))
    time = int( input("How many hours has it traveled? "))

    print("Hour","\tDistance Traveled")
    print("-----------------------------")

    for hour in range(1, time + 1):
        distance = speed * hour
        print( hour,"\t",distance )

main()
    
    
