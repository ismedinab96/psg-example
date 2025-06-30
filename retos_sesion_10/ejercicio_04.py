#Jane y Jhon llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a un candy bar. 
# Quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. 
# A continuación tienes los postres que han ido pidiendo en cada salida:

#Si la cantidad de postres que tienen en común es mayor al 50%
# entonces son compatibles, de lo contrario quieren replantear su relación

Jane =  {"Lemon Pie", "Brownie", "Tarta de Manzana","Helado de Chocolate","Flan"}
Jhon =  {"Carrot Cake", "Croissant de Chocolate","Lemon Pie", "Tarta de Manzana", "Pudding"}

gustos_compatibles = Jane.intersection(Jhon)
total= len(Jane) + len(Jhon)
compatibles = len(gustos_compatibles) / total 
if compatibles >= 0.5:
    print("Son compatibles!! Su relacion tiene futuro")
else: print("Deben replantear su relacion")
