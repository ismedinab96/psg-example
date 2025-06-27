#Una dulcería tiene 2 listas una con los productos y otra con los precios
# Agregar 2 productos nuevos al final de las listas
# Eliminar el producto con el nombre "Bon Bon Bum" de las listas
# ¿Cuánto cuesta el producto "Oreo" y "Chizitos"?    
# ¿Cuál es el producto más caro y el más barato?
# ¿Cuántos productos tienes en total?
# ¿Cuanto cuestan todos los productos?
# Ordena los productos y precios del más barato al más caro
# Eliminar todos los productos de las lista

productos = ["Oreo","Chizitos","Pipocas","Come Come","Papitas","Bom Bon Bum"]
precios = [8 , 2.5 ,2.5 ,3 , 3, 1.5]

productos.append("Olitas")
precios.append(5)
print(productos)
print(precios)

productos.append("Chicharron")
precios.append(2)

print(productos)
print(precios)

indice = productos.index("Bom Bon Bum")
precios.pop(indice)
productos.pop(indice)

print(productos)
print(precios)

print(f'Precio maximo: {max(precios)}  y precio minimo: {min(precios)}')

print(f' productos totales: {len(productos)}')

print(f'Precio total: {sum(precios)}')

precios.sort()
productos.sort()

print(productos)
print(precios)

productos.clear()

print(productos)




