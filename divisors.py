'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)'''

num=int(input("enter a number: "))
limit=num+1

divisor_list=[]

for i in range(1,limit):
    if num % i == 0:
        divisor_list.append(i)
        #print(i)
print(divisor_list)
