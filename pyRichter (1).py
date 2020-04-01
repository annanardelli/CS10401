#PYTHON RICHTER SCALE CALCULATION
#Your first and last name: Anna Nardelli
#Your ID: 1164308

#REQUIREMENTS:
# ask the user to "Enter the Richter scale value or -99 to end: "
# the program must end when the user enters -99
# the richter scale value entered must be greater than 0
# if the richter scale value is less than 0, the program must print  "Value must be greater than 0"
#   and the user must re-enter the richter scale value
# program must print the correct warning message for the richter scale value entered as per the accompanying diagram
# program must print only 1 warning message for each richter scale value entered
# the program must be tested so that it repeats until user enters -99
# the program must be tested so that if user enters a richter scale value less than 0,
#   "Value must be greater than 0" prints and the user must re-enter it
# the program must be tested with each of the following values to make sure the correct warning message is printed
#    8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6
#-------------------------------------------------------------------------

# HINT: Use the base number conversion program for guidance
#--------------------------------------------------------------------------------------------
# 1. Develop the ALGORITHM for Richter Scale program from the requirements and enter it below
#--------------------------------------------------------------------------------------------
#1. Ask the user to enter the value
#2. Make sure that the value is greater than zero
#3. If the value is less than zero, ask the user to enter another value
#4. If the value is -99, end the program
#5. If the value is >= 8, "Most structures fall."
#6. If the value is >= 7, "Many buildings destroyed."
#7. If the value is >=6, "Many buildings considerably damaged, some collapse."
#8. If the value is >=4.5, "Damage to poorly constructed buildings."
#9. If all are false, "No destruction of buildings."
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 2. Convert the ALGORITHM to PSEUDOCODE and enter it below
#-------------------------------------------------------------------------
#Ask the user to "Enter the Richter scale value or -99 to end: "
#If the value < 0, print "Value must be greater than 0"
#User must reenter values until one is greater than 0.
#If the value is -99, end the program
#If the value is less than zero, print "Value must be greater than 0"
#If the value is greater than or equal to 8, print "Most structures fall."
#If the value is greater than or equal to 7, print "Many buildings destroyed."
#If the value is greater than or equal to 6, print "Many buildings considerably damaged, some collapse."
#If the value is greater than or equal to 4.5, print "Damage to poorly constructed buildings."
#If the value is greater than or equal to 0, print "No destruction of buildings."
#Repeat until the user enters -99
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 3. Convert the PSEUDOCODE into PYTHON CODE and enter it below
#-------------------------------------------------------------------------
keepgoing=True
while keepgoing==True:
    value=float(input("Enter the Richter scale value or -99 to end:"))
    if value== -99:
        keepgoing=False
        exit()
    while (value!=-99):
        if value<=0:
            print("Value must be greater than 0")
            break
        elif value>=8:
            print("Most structures fall.")
            break
        elif value>=7:
            print("Many buildings destroyed.")
            break
        elif value>=6:
            print("Many buildings considerably damaged, some collapse.")
            break
        elif value>=4.5:
            print("Damage to poorly constructed buildings.")
            break
        elif value>=0:
            print("No destruction of buildings.")
            break

    






