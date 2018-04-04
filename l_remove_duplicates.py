'''
Write a program (function!) that takes a list
Returns a new list that contains all the elements of the first list minus all the duplicates.
'''

import random

def CreateList(limit):
    original_list = []
    new_list = []
    print("enter the list elements: ")
    for x in range(1,limit):
        num = int(input())
        original_list.append(num)
    for x in original_list:
        if x not in new_list:
            new_list.append(x)
    return new_list

def CreateSet(limit):
    original_list = []
    new_set = []
    print("enter the list elements: ")
    for x in range(1,limit):
        num = random.randint(1,100)
        original_list.append(num)
    print("original list {}".format(original_list))
    new_set = set(original_list)
    return new_set

def main():
    ch = 'y'
    while ch == 'y':
        limit = int(input("enter the list limit"))
        print("enter choice of user ")
        print("1.Create List by loop 2.Create set ")
        ch = int(input())
        if ch ==1:
            new_list = CreateList(limit)
            print(new_list)
        else:
            new_set = CreateSet(limit)
            print(new_set)
        print("Do you want to continue ? (y/n)")
        ch = input()

if __name__=="__main__":
    main()
