# we will learn what is slicing today 
# suppose i want to slice a list

list = [1,2,3,4,5,6]

# sliced the first item
for items in list[1:]:
  print (items)

#sliced the 1,2,6
for items in list[2:5]:
  print (items)


#Tuple can be sliced in the same way

tuple = ("a","b","c","d")

for tup in tuple[1:]:
  print(tup)