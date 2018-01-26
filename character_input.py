'''Create a program that asks the user to enter their name and their age.
 Print out a message addressed to them that tells them the year that they will turn 100 years old.'''


name = input("enter the name: ")
age =  int(input("enter age: "))
year = int(input("enter the current year: "))
yr=(100-age)+year
print(name +" will turn 100 in the year {} ".format(yr))
