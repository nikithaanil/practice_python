#Ask the user for a string and print out whether this string is a palindrome or not.
#A palindrome is a string that reads the same forwards and backwards.)

string = input("enter the string to check: ")
length = len(string)
#print(length)
flag=0
y=int(length/2)
#print(y)
x=0
while x < y :
    if string[x] != string[length-1]:
        flag=0
    else:
        flag=1

    x=x+1
    length=length-1

if flag==0:
        print("it is not a palindrome")
else:
        print("it is a palindrome")
