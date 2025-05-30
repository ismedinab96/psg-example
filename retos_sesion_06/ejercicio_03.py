#3.- Imprime una tabla de verdad para la siguiente sentencia: 
# "Un sistema de seguridad controla el acceso a una habitación, la puerta sólo se abre si se introduce una tarjeta válida o la huella dactilar, 
# pero no ambas al mismo tiempo. Si se introduce la tarjeta y la huella dactilar, la puerta no se abre. ¿Qué operador lógico se puede utilizar?"



#Utiliza el operador logico OR, porque solo una condicion puede ser cierta, no ambas
#T_V = Tarjeta Valida; H_D = Huella Digital
print("T_V  |  H_D | Puerta    ")
print("_____|______|___________")
print("False| False| No se Abre")
print("False| True | Se Abre   ")
print("True | False| Se Abre   ")
print("True | True | No se Abre")