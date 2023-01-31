### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))# Inicialmente es un diccionario

my_other_set = {'Alvaro', 'Casco', 16}
print(type(my_other_set))

print(len(my_other_set))

# Insercion

my_other_set.add("Andres") 

print(my_other_set)# un set no es una estructura ordenada

my_other_set.add('Andres')# un set no admite repetidos

print(my_other_set)

# Busqueda

print("Alvaro" in my_other_set)
print("Alvari" in my_other_set)

# Eliminacion

my_other_set.remove("Alvaro")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) name 'my_other_set' is not definited

my_set = {"Alvaro", "Casco", 16}
my_list = list(my_set)
print(my_list)
print(my_list[0])

# Transformacion

my_other_set = {"Javascript", "C++", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Html", "C#"}))

print(my_new_set.difference(my_set))

