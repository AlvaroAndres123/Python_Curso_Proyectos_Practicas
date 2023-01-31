### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
   def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

   def get_name(self):
        return self.__name


my_person = Person("Alvaro", "Casco")
print(my_person.full_name)
my_person.walk()
0
my_other_person = Person("Alvaro", "Casco", "Temerario")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Maria Casco (La Sol)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)