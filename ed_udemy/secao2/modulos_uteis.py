import math, datetime
x = math.sqrt(9)
seno = math.sin(45)
coseno = math.cos(45)
log = math.log(1000,10)
log2 = math.log(32,2)
euler = math.e
pi = math.pi

print("raiz quadrada ",x)
print("seno ", seno)
print("cosseno ", coseno)
print("logaritmo 1 ", log)
print("logaritmo 2 ", log2)
print("valor de euler ", euler)
print('valor de pi ', pi)

print(" ")
print("Modulo de data *** ")
print(dir(datetime))
hoje = datetime.date.today()
hora = datetime.datetime.now()
data = datetime.date(2021,12,15)

print("data de hoje: ", hoje)
print("são ", hora)
print("data ", data)
print("Hoje é dia ", data.day,hoje.day)
print("estamo no mês ", data.month, hoje.month)
print("ano de ", data.year, hoje.year)

print("hora:  ", hora.hour)
print("minutos: ", hora.minute)
print("segundos: ", hora.second)