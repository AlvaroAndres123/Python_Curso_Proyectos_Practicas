# Variables

from operator import le

my_variable = "My String Variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_variable)
print(type(my_int_to_str_variable))

# Concatenation of variables in a print
print(my_variable, my_int_variable, my_bool_variable)
print('This is the value of:', my_bool_variable)

# Some system fuctions
print(len(my_variable))

# Variables in one line
name, surname, alias, age = "Alvaro", "Casco", "Gordo", 35
print("My name is:", name, surname, ". My age is:", age,". And my alias is:", alias)

name = input('What is your name: ')
age = input('How old are you: ')

print(name)
print(age)

# Change his type
name = 16
age = "Alvaro"
print(name)
print(age)

# ¿We force the type?
address: str = "My Address"
address = True
address = 5
address = 1.2
print(type(address))