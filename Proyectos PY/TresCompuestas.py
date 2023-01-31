### Hacer ejercicios de tres ###
def compuesta():
 a = int(input("Inserte el valor a: ")) 
 b = int(input("Inserte el valor de b: "))
 c = int(input("Inserte el valor c: "))
 d = int(input("Inserte el valor de d: "))
 e = int(input("Inserte el valor e: "))
 first_relation = input("Tu primera relacion es directa o inversa: ")
 second_relation = input("Tu segunda relacion es directa o inversa: ")
 if first_relation == "directa" and second_relation == "inversa":
      print(b * c * e / (a * d))
 elif first_relation == "inversa" and second_relation == "directa":
      print(a * d * e / (b * c))
 elif first_relation == "directa" and second_relation == "directa":
      print(b * d * e / (a * c))
 elif first_relation == "inversa" and second_relation == "inversa":
      print(a * c * e / (b * d))



def simple(): 
 a = int(input("Inserte el valor a: ")) 
 b = int(input("Inserte el valor de b: "))
 c = int(input("Inserte el valor c: "))
 relation = input("Tu relacion es directa o inversa: ")
 if relation == "directa":
      print(b * c / a)
 elif relation == "inversa":
     print(a * b / c)

menu = input("""
  Regla de tres 
  Selecciona el tipo
  1. Regla de tres simple
  2. Regla de tres compuesta
  """)

if menu == "1":
   print(simple())   
elif menu == "2":
   print(compuesta())


# Regla de tres compuesta

    


# Regla de Tres Simple


