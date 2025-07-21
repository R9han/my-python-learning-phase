# Typecasting : the process of converting a variable one data type to another 
#                   str(), int(), float(), bool()     

name = "Rohan"
name_2 = ""
age  = 88 
age_2 = 99
gpa  = 4.75 
is_student = True 



print(type(is_student)) # you can check the data type by doint this and you will get the ans like this: <class 'bool'> 

age = float(age)
print(age)

age_2 = str(age_2)
age_2 += "1"  #  here 1 is a string
print(age_2) # expected ans is: 991 

name = bool(name)
print(name) # the answer you will see: True 

name_2 = bool(name_2)
print(name_2)    # in this case, you will see the answer is: False 