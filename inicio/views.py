from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

import random


def inicio(request):
    return HttpResponse('Bienvenidos a mi INICIO!')


def template1(request,nombre,apellido,edad):
    fecha = datetime.now()
    suma = 4 + edad
    
    return HttpResponse(f'<h1>Mi Template 1</h1> -- Fecha:{fecha} -- Buenas {nombre} {apellido} {edad}')


# h1 indica que es un titulo lo muestra como tal, se arman de mayor a menor importancia del h1 al h6 titulo subtitulo etc

def template2(request, nombre, apellido, edad):
    
    archivo_abierto = open(r'C:\Users\Day\Desktop\programacion\miproyecto\templates\template2.html')
    # archivo_abierto = open('templates/template2.html')
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    
    fecha = datetime.now()
    
    datos = {'fecha':fecha,
             'nombre':nombre,
             'apellido':apellido,
             'edad':edad,
             }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)
 # Agregar la r para que python sepa que es una ubicacion de archivo y no rompa el codigo
 
#v3
def template3(request, nombre, apellido, edad):
    
    template = loader.get_template('template2.html')
    
    fecha = datetime.now()
    
    datos = {'fecha':fecha,
             'nombre':nombre,
             'apellido':apellido,
             'edad':edad,
             }
    
     
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)
 
 #v4
 
def template4(request, nombre, apellido, edad):
    
   
    fecha = datetime.now()
    
    datos = {'fecha':fecha,
             'nombre':nombre,
             'apellido':apellido,
             'edad':edad,
             }
    
    
    return render(request,'template2.html', datos)

''' tmb se puede hacer asi: 

    return render(request,'template2.html',  datos = {'fecha':fecha,
             'nombre':nombre,
             'apellido':apellido,
             'edad':edad,
             }
    )
    
    return render(request,'template2.html', {})
    
 '''
 
def probando(request):   
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    print(numeros)
    return render(request,'probando_if_for.html',{'numeros': numeros})
 
 
 
 