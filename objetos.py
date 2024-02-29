

# Para crear un objeto la palabre clave es class
# La clase funciona como un cubo de Minecraft, como una plantilla
# para crear objetos (o personas)

# Primero atributos de lo que consideramos un objeto (o persona)

class Persona:  #self hace referencia a lo que será el objeto
    def __init__(self, nombre: str, edad: int,                 
                 pelicula_favorita: str):
        
        # Constructor de clase que construye los atributos del objeto
        self.nombre = nombre 
        self.edad = edad
        self.pelicula_favorita = pelicula_favorita

    # Método: una función que está dentro de una clase
    def presentarse(self):
        print(f"Buenas tardes, ¿cómo va la energía?, me conocen como {self.nombre}, tengo casi {self.edad} mirrey, y estoy matado con {self.pelicula_favorita}")
        

valen = Persona('San Valen', edad= 30, pelicula_favorita= 'Alguna cinta rumaní')

print(valen)      
print(valen.presentarse())
# Los métodos van entre paréntesis
# Esto genera reuso porque puedo presentar otra persona


class Animal:

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def hacer_sonido(self):
        pass

tigre = Animal('Táiguer')

print(tigre)
print(tigre.nombre)        
print(tigre.hacer_sonido())      

class Perro(Animal):

    def hacer_sonido(self):
        return 'WOW COMO EL FERXXO '
    
class Gato(Animal):
    def hacer_sonido(self):
        return 'Raw (mero sonido todo raro) '
    
perro = Perro('Trotsky')
gato = Gato('Shibi')

print(
    f"La gata se llama {gato.nombre} y hace {gato.hacer_sonido()}"
)

print(
    f"El perro se llama {perro.nombre} y hace {perro.hacer_sonido()}"
)

# Estoy heredando propiedades de la clase animal a la clase perro y la clase gato,
# también aquí ocurrió un polimorfismo, esto se mejora haciendo ejemplos

