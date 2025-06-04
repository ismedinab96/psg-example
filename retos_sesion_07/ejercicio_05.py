#Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome sin importar los espacios, mayúsculas o minúsculas
palabra = input("Ingrese una palabra: ")
palabra_mod = palabra.replace(" ","").lower()
palindromo = print(True) if palabra_mod[len(palabra_mod)::-1] == palabra_mod else print(False)


