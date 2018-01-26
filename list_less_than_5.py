n=int(input("\nenter the limit "))
print("enter the elements ")
arr=[]
newlist=[]
for i in range(0,n):
    arr.append(int(input()))

#print(arr)
for x in arr:
    if x< 5:
        newlist.append(x)
        #print(x)
print(newlist)
