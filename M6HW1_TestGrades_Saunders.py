# Computes average of five test grades
# November 10, 2017
# CTI-110 M6HW1- Test Average and Grade
# Laura Saunders
#

# This program will ask the user to enter five test grades.
# This program will display a letter grade for each score.
# This program will display the average test score.

# A_score: 90-100
# B_score: 80-89
# C_score: 70-79
# D_score: 60-69
# F_score: Below 60


def calc_average( score1, score2, score3, score4, score5 ):
    average = ( score1 + score2 + score3 + score4 + score5 ) / 5
    return average

def determine_grade (score):
    if (score < 60):
        return "F"
    elif (score < 70):
        return "D"
    elif (score < 80):
        return "C"
    elif (score < 90):
        return "B"
    elif (score < 101):
        return "A"


def showResults( score1, score2, score3, score4, score5 ):
    print( "\nScore\tLetter Grade\n" )
    print( str( score1) + "\t" + determine_grade( score1 ),\
           str( score2) + "\t" + determine_grade( score2 ),\
           str( score3) + "\t" + determine_grade( score3 ),\
           str( score4) + "\t" + determine_grade( score4 ),\
           str( score5) + "\t" + determine_grade( score5 ), sep = "\n" )
    

def main():
    # User should input five test scores.
    score1 = float( input( "Enter test score 1: "))
    score2 = float( input( "Enter test score 2: "))
    score3 = float( input( "Enter test score 3: "))
    score4 = float( input( "Enter test score 4: "))
    score5 = float( input( "Enter test score 5: "))

            
    showResults( score1, score2, score3, score4, score5 )
    
    print( "The average is", calc_average( score1, score2, score3, score4, score5 ) )
    
    

main()

    
    
