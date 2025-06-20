name = "riziya"
age = 7
is_student = True
weight = 15.5

print("your name is ", name)
print("Data type of name is", type(name))
print("your age is ", age)
print("Data type of age is ", type(age))
print("is student: ", is_student )
print("is_student data type is ", type(is_student))
print("your weight is", weight)
print("data type of weight is ", type(weight))

# after type casting
print("after type casting")
age = str(age)
print("data types of age", type(age))
weight = int(weight)
print("data type of weight", type(weight))
