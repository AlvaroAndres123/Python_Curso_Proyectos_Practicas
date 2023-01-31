### Functions ###

def my_function():
    print("Esto es una funcion")
    

my_function()
my_function()
my_function()

def sum_two_values (first_value : int, second_value : int):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values("5","7" ) 
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value : int, second_value : int):
   my_sum = first_value + second_value
   return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)


def print_name (name,surname):
    print(f"{name} {surname}")


print_name(surname="Casco", name= "Alvaro")

def print_name_with_default (name,surname,alias = 'Sin Alias'):
    print(f"{name} {surname} {alias}")

print_name_with_default("Alvaro", "Casco")
print_name_with_default("Alvaro", "Casco", "Temerario")

def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("Hola", "Python", "Almasoft")
print_texts("Hola")