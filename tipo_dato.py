# Definición de variables


x = 20

print(x*2)

# Tipos de dato

nombre = 'Valentín' # string
edad = 27 # integer int
estatura = 1.77 # float
is_profesor = True # es tipo bool (False)

# Ejemplo. ¿Puedo sumar dos string?
# Sí se puede

apellido = 'Ospina'

nombre_completo = nombre + ' ' + apellido
print(nombre_completo)
edad = 'perro'
print(edad)

# Ejemplo de como se suman dos strings

def suma(a,b):
    """suma de dos números"""
    return a + b
print(suma('2','3'))

# Función mal definida
def multi(c,d):
    return c*d
# print(multi('2','3')) # ejemplo de un error

# Listas

Lista = [1,2,3,89,3,'6', True, 8.0,] 

print(Lista[0], Lista[6])

for value in Lista:
    print(value)

Lista[0] = 'mi fai'
Lista.append(89)

print(Lista)

# Tuplas: se diferencian en las listas en que son inmutables

tupla = ('funk',36, False, 650.00)

conjunto = {1,3,4,5,5,5,5,5,5,5,5,5}

# Ejercicio: 

""" Dada la lista lista_con_dup = [1,1,2,2,3,4,5,6,6,6] construir una lista con 
los mismos elementos pero sin duplicado. HInt: use list y set"""

lista_con_dup = [1,1,2,2,3,4,5,6,6,6] 

sin_dup =  list(set(lista_con_dup)) # se convierte en conjunto y luego en lista de nuevo

print(sin_dup)

diccionario = {
    'nombre':'Valentín',
    'ocupación':'Statistician',
    'profesión' :'En extensión de ingeniería mi rey'
}


for value in diccionario.keys():
    print(key)
