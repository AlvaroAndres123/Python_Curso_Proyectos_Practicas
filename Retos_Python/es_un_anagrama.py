'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''
def is_anagram(one_word, two_word):
    if one_word.lower() == two_word.lower():
        return False
    return sorted(one_word.lower()) == sorted(two_word.lower())

print(is_anagram("Amor", "roma"))