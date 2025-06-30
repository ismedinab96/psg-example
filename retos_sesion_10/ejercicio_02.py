#El dueño de una tienda de ropa deportiva ha comprado ropa formal y quiere abrir una nueva tienda que combine ambos estilos.
# Crea un conjunto con las prendas de ambos tipos con las listas de prendas
lista = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
lista2 = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

conjunto_nuevo = set(lista)
conjunto_nuevo.update(lista2)
print(conjunto_nuevo)