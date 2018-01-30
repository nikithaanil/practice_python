#a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

c=set(a)
d=set(b)
diff=[]
for x in c:
    for y in d:
        if x==y:
            diff.append(x)
            #print(x)

print("the common elements are")
print(diff)
