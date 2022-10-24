import datetime
import time
data = datetime.date.today()
dia = datetime.date.today().day
mes = datetime.date.today().month
ano = datetime.date.today().year

diaatual = datetime.date.isoformat(datetime.date.today())
hora = time.strftime("%H:%M %A %p")
semana = time.strftime("%A %p")

print(data)
print(f'{dia}/{mes}/{ano}')
print(diaatual)
print(hora)
print(semana)
