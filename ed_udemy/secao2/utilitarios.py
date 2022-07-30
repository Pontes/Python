def soma(a,b,c):
    somatorio = a+b+c
    return somatorio

def mult(a,b,c):
    produto = a*b*c
    return produto

def palindromo(string):
    if string == string[::-1]:
        return True
    else:
        return False

def div(a,b):
    return a/b