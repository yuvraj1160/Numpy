list1 = [1,3,5]
list2 = [4,6,7]

result = [x+y for x,y in zip(list1, list2)]
print(result)