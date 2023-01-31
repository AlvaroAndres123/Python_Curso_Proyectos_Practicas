## Tuples ##

my_tuple = tuple()
my_other_tuple = (35, 60, 30)

my_tuple = (16, 1.80, "Alvaro", "Casco", "Casco")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6])

print(my_tuple.count("Alvaro"))
print(my_tuple.index("Casco"))
print(my_tuple.index("Alvaro"))

#my_tuple[1] = 1.80 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "AlmaSoft"
my_tuple.insert(1,"Azul")
print(tuple(my_tuple))
print(type(my_tuple))

#del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion 

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined
