

# Para crear un objeto la palabre clave es class
# La clase funciona como un cubo de Minecraft, como una plantilla
# para crear objetos (o personas)

# Primero atributos de lo que consideramos un objeto (o persona)

class Persona:
    def __init__(self, nombre: str, edad: int,   #self hace referencia a lo que será el objeto
                 pelicula_favorita: str):
        
        # Constructor de clase que construye los atributos del objeto
        self.nombre = nombre 
        self.edad = edad
        self.pelicula_favorita = pelicula_favorita

    # Método: una función que está dentro de una clase
    def presentarse(self):
        print(f"Buenas tardes, ¿cómo va la energía, me conocen como {self.edad}, tengo {self.edad} años de edad, y estoy matado con {self.pelicula_favorita}")
        

valen = Persona('San Valen', edad= 27, pelicula_favorita= 'Taxi Driver')

print(valen)      
print(valen.presentarse())
# Los métodos van entre paréntesis
# Esto genera reuso porque puedo presentar otra persona


         
        