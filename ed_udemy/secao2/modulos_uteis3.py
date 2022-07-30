import time as tm
x = tm.time()

antes = tm.time()
lista =[]
for i in range(0,100000):
    lista.append(i)
depois = tm.time()
interv = depois - antes

print("tempo em segundos: ", x)
print()
print("********************")
print("execução de código")
print("tempo antes: ", antes)
print("tempo depois:", depois)
print(f'tempo: {interv} segundos')
print("********************")
print()
print("finalizando....")
tm.sleep(2)
print("...")
tm.sleep(2)
print('até a próxima!')

