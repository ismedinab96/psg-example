notas = (10,61,00,21,22,0,32,30,41,51,5,23,100)
promedio = sum(notas) / len(notas)
aprobo = "Aprobo" if promedio >= 51 else "Reprobo"
resultado =(round(promedio,4),aprobo)
print(resultado)
