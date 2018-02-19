''' Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
Make a new list of only the first and last elements of the given list.'''

list1 = []

def newlist(limit):
    
    list2 = []
    print("enter the elements: ")
    while(limit > 0):
        n = int(input())
        list1.append(n)
        limit = limit-1
    list2.append(list1[0])
    list2.append(list1[-1])
    print(list2)




def main():

    n = int(input("enter the limit: "))
    newlist(n)

if __name__ == "__main__":
    main()
