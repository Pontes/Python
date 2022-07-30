
def somaAte(x):
    num = 0
    n=x*(x+1)//2

    for i in range(1,x+1):
        num = num + i
    
    return n
    

n = somaAte(10)
print("Valor de n: ", n)
