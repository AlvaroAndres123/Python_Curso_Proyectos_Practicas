### Arithmetic Operators ###

# Operations with integers
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operations with strings
print("Hello " + "Python " + "¿What's up?")
print("Hello " + str(5))

# Mixed Operations
print("Hello " * 5)
print("Hello" * (2 ** 3))

my_float = 2.5 * 2
print("Hello " * int(my_float))

### Comparative Operators ###

# Operations with integers
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operations with strings
print("Hello" > "Python")
print("Hello" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hello" <= "Python")
print("Hello" == "Hola")
print("Hello" != "Python")

### Logical operator ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hello" > "Python")
print(3 > 4 or "Hello" > "Python")
print(3 < 4 and "Hello" < "Python")
print(3 < 4 or "Hello" > "Python")
print(3 < 4 or ("Hello" > "Python" and 4 == 4))
print(not (3 > 4))