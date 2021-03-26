#Arithmatic operations
#+, - , * , / , % (modulus) , ** (exponential), // (floor division) are arithmatic operations in python
#How many minutes are there in 20 days?
#20 *24 *60

#this will give you the answer
print(20*24*60)

#to make it meaningful
print("These are the minutes in 20days")
print(20*24*60)

#or
print("These are the minutes in 20days ",20*24*60 )

#or you can use string concatination, i.e making a non string value as string using str()

print("There are "+ str(20*24*60)+ " minutes in 20 days")

#or a more systematic way of using string concatination is using a 'f' in the begining and use {} for the non string part. this feature is available in latest version of python.
print(f"There are {20*24*60} minutes in 20 days")
