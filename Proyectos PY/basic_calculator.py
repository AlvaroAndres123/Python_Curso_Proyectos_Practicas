
def selection_of_operation(valor1, valor2):
  selection = input("Seleccione La Operacion que desea Realizar\n 1. Suma\n 2. Resta\n 3. Division\n 4. Multiplicacion\n")
  final_selection = selection.upper()
  if final_selection != "SUMA" and final_selection != "RESTA"and final_selection != "DIVISION" and final_selection != "MULTIPLICACION":
   print("Ingrese una operacion correcta")
   return selection_of_operation()
  elif final_selection == "SUMA":
   return suma(valor1 + valor2)
  elif final_selection == "RESTA":
   return resta(valor1 - valor2)
  elif final_selection == "DIVISION":
   return resta(valor1 / valor2)
  elif final_selection == "MULTIPLICACION":
   return resta(valor1 * valor2)

def other_op():
     other_operation = input("Quiere hacer otra operacion Y/N\n")
     other_operation = other_operation.upper()
     if other_operation == "N":
        print("Ok se ha terminado la consulta")
        exit()
     elif other_operation == "Y":
        return selection_of_operation(5, 5)
     else:
        print("Seleccione Y o N")
        return other_op()

def suma(suma_valor):
    print(f"El resultado de la suma es {suma_valor}")
    other_op()
    
def resta(suma_valor):
    print(f"El resultado de la resta es {suma_valor}")
    return other_op()

def division(suma_valor):
    print(f"El resultado de la division es {suma_valor}")
    other_op()

def multiplicacion(suma_valor):
    print(f"El resultado de la multiplicacion es {suma_valor}")
    other_op()



selection_of_operation(5, 5)