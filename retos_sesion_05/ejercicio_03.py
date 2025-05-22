#Ejercicio 3
# Escribe un programa en Python que convierta 1000000 de segundos en semanas, días, horas, minutos y segundos

#Solucion
#Tomamos en cuenta que: 
# 1 minuto = 60 s
# 1 hora = 3600 s
# 1 dia = 86400 s
# 1 semana = 604800 s
tiempo_s = 1000000
semanas = tiempo_s // 604800
dias = (tiempo_s % 604800) // 86400
horas = (tiempo_s % 86400) // 3600
minutos = (tiempo_s % 3600) // 60
segundos = (tiempo_s % 60)

print("1000000 s equivale a: ",semanas," semana, ",dias," dias, ",horas," horas, ",minutos," minutos y ",segundos," segundos")