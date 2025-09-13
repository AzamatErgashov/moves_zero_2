# first solution

l = 0
mylist = [0,1,2,4,5,0,6]

for i in range(len(mylist)):
    if mylist[i] != 0:
        mylist[l], mylist[i] = mylist[i], mylist[l]

        l += 1

print(mylist)

# second solution

count = 0
mylist = [0,1,2,4,5,0,6]

for i , num in enumerate(mylist):
    if num == 0:
        count += 1
        continue

    mylist[i], mylist[i-count] = mylist[i-count], mylist[i]

print(mylist)
