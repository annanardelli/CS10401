wholeString=input("Please enter your last name, first name, your favorite color, your favorite animal, and your favorite team: (ex: Eckert, Gil, blue, dog, hawks):")
commaLocation1=wholeString.find(",")
wholestringLength=len(wholeString)
lastNameLength=len(wholeString[0:commaLocation1])
lastName=wholeString[0:commaLocation1]
firstNameString=wholeString[commaLocation1+2:wholestringLength]
commaLocation2=firstNameString.find(",")
firstName=firstNameString[0:commaLocation2]
colorString=firstNameString[commaLocation2+2:wholestringLength]
commaLocation3=colorString.find(",")
color=colorString[0:commaLocation3]
animalString=colorString[commaLocation3+2:wholestringLength]
commaLocation4=animalString.find(",")
animal=animalString[0:commaLocation4]
teamString=animalString[commaLocation4+2:wholestringLength]
team=teamString
team=team.capitalize()
print("My name is " + firstName +" "+ lastName + ", my favorite color is " + color + ", my favorite animal is a " + animal + ", and my favorite team is the " + team +".")

