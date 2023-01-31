'''
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

def area(perimetro, apotema):
    form = (input("Que Figura es tu poligono\n1.Triangulo\n2.Cuadrado\n3.Rectagulo\n"))
    final_form = form.capitalize()
    if final_form == 1 or "TRIANGULO":
       print(perimetro * 3 * apotema / 2)
    elif final_form == 2 or "CUADRADO":
        print(perimetro * 4 * apotema / 2)
    elif form == 2 or "CUADRADO":
        print(perimetro * 4 * apotema / 2)
    else:
        print("Ponga Una Figura Correcta")
        return form


area(6, 4.1)