num=[20,5,6,89,3,88]
numbers=num.copy()
num.append(22)
num.insert(2,10)# nums.insert(index,number)
print(num)
num.remove(5)
print(num)
# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
num.pop()
print(num)
# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes 
# and returns the last item in the list. (The square brackets around the i in the method signature denote that 
# the parameter is optional, not that you should type square brackets at that position. You will see this notation 
# frequently in the Python Library Reference.)

# list.clear()
# Remove all items from the list. Equivalent to del a[:].
print(num.index(20))# returns the first occurence of index of the number
# print(num.index(2))-> returns error if the number is not present in the list

print(10 in num)# generates true or false, better than list.index
print(num.count(10))# returns the number of occurences in the list
num.sort()# sorts the list in ascending order
print(num)
num.reverse()# reverses the list 
print(num)
print(numbers)
