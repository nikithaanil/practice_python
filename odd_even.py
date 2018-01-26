'''Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user
'''
num=int(input("enter the number to be checked: "))
result=num%2

if result == 0:
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))

#if num%4==0:
#    print("{} is a multiple of 4".format(num))
