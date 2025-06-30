tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

tienda_fis = set(tienda_fisica)
tienda_on = set(tienda_online)

#a. Quiénes compraron en ambos canales.
compraron_ambos = tienda_fis.intersection(tienda_on)
print(f'Compraron en ambas tiendas: {compraron_ambos}')
#b. Quiénes compraron solo en la tienda física.
solo_tiendafis = tienda_fis.difference(tienda_on)
print(f'Solo compraron en la tienda fisica: {solo_tiendafis}')
#c. Quiénes compraron solo online.
solo_tiendaon = tienda_on.difference(tienda_fis)
print(f'Solo compraron en la tienda online: {solo_tiendaon}')