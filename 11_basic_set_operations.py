my_set = {"January", "February", "March"}
# we cannot access individual elements of a set
# print(my_set[0])

# instead we can print all elements using loop
for i in my_set:
    print(i)

#add element
my_set.add("april")
print(my_set)

#you can see the order changes each time u run
#to remove an element
my_set.remove("January")
print(my_set)