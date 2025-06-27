#Crear una lista de personas con 10 nombres de personas
# Obtener una sub lista de 5 a 9 con saltos de 2 en 2
# Buscar si existe el nombre "José" en la lista original
# Ordenar la sub lista alfabéticamente a-z
# Ordenar la lista original alfabéticamente descendente z-a

nombres = ["Carlos", "Jose", "Maria","Carla","Daniela","Miriam","Fernanda","Jhonny","Antelo","Josef"]
print(nombres[5:9:2])
print(nombres.index("Jose"))
nombres.sort()
print(nombres)
nombres.sort(reverse=True)
print(nombres)
