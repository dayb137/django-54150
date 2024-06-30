def deco(func):
    def funcion():
       print('Primer print de deco')
       func()
       print('segundo print de deco')
    
    return funcion

@deco   
def suma(a, b):
    return a+b

print(f'El resultado de la suma entre 2 y 2 es',suma(2,2))
