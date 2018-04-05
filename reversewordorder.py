'''
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
For example, say I type the string:
'''

teststring = "My name is Nikitha Anil"
teststring = teststring.split()[::-1]
print(teststring)
