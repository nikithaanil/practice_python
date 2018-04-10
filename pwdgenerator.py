'''
Write a password generator in Python.
Be creative with how you generate passwords.
Strong passwords have a mix of lowercase letters,uppercase letters,numbers,and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
'''

import random
import string

ch = 'y'

while ch =='y':
    print("enter the type of password preferred")
    ch = int(input("1.Weak password"+"\n"+"2.Strong Password"))
    length = int(input("enter the length of password: "))
    password = []

    if ch==1:
        for i in range(1,length+1):
            alp = random.choice('abcdefghijklmnopqrstuvwxyz')
            password.append(alp)
        password=''.join(password)
        print(password)

    if ch==2:
        for i in range(1,length+1):
            alpnum = random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
            password.append(alpnum)
        password=''.join(password)
        print(password)
    ch = input("do you want to continue (y/n)?")
