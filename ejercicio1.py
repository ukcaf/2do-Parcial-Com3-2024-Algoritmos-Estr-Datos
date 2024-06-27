#ejercicio1
from datetime import date, datetime

class Fecha:
    def __init__(self, dia=None, mes=None, año=None):  #arranca instancia de la clase "fecha". si no se agregan datos se establece la fecha actual
        if dia is None or mes is None or año is None:
            hoy = date.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.año = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.año = año
    
    def __str__(self):      #devuelve la fecha en formato dd/mm/aaaa
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"
    
    def __add__(self, other): #calcula la diferencia en dias entre dos fechas
        if isinstance(other, Fecha):
            return self.calcular_dif_fecha(other)
        else:
            raise TypeError("El objeto debe ser de tipo Fecha")
    
    def __eq__(self, other):     #compara dos objetos de clase "fecha" para ver si son iguales 
        if isinstance(other, Fecha):
            return self.dia == other.dia and self.mes == other.mes and self.año == other.año
        else:
            return False

    def calcular_dif_fecha(self, otra_fecha):   #calcula la diferencia en dias entre las fechas proporcionadas
        fecha1 = date(self.año, self.mes, self.dia)
        fecha2 = date(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        diferencia = abs((fecha2 - fecha1).days)
        return diferencia

# Ejemplo de uso:
fecha1 = Fecha(24, 5, 2024)
fecha2 = Fecha(1, 1, 2025)
fecha_hoy = Fecha()

print(f"Fecha 1: {fecha1}")
print(f"Fecha 2: {fecha2}")
print(f"Fecha de hoy: {fecha_hoy}")
print(f"Diferencia entre Fecha 1 y Fecha 2: {fecha1.calcular_dif_fecha(fecha2)} días")
print(f"¿Fecha 1 es igual a Fecha 2?: {fecha1 == fecha2}")


#ejercicio2
class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):    #diccionaro de datos del alumno
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }

    def cambiar_datos(self, **nuevos_datos):  #permite actualizar los dtos del alumno
        for key, value in nuevos_datos.items():
            if key in self.datos:
                self.datos[key] = value
            else:
                print(f"Clave '{key}' no existe en los datos del alumno.")

    def antiguedad(self):  #calcula la la antiguedad en años desde la fecha de ingreso
        hoy = date.today()
        antiguedad = hoy.year - self.datos["FechaIngreso"].year - ((hoy.month, hoy.day) < (self.datos["FechaIngreso"].month, self.datos["FechaIngreso"].day))
        return antiguedad

    def __str__(self):
        return f"Alumno(Nombre: {self.datos['Nombre']}, DNI: {self.datos['DNI']}, FechaIngreso: {self.datos['FechaIngreso']}, Carrera: {self.datos['Carrera']})"

    def __eq__(self, otro):  #compara si dos "alumno" tienen el mismo DNI
        if isinstance(otro, Alumno):
            return self.datos["DNI"] == otro.datos["DNI"]
        return False

# Ejemplo de uso:
alumno1 = Alumno("Lionel Messi", 12345678, date(2020, 3, 1), "Bellas Artes")
alumno2 = Alumno("Angel Di Maria", 87654321, date(2019, 7, 15), "Medicina")

print(alumno1)
alumno1.cambiar_datos(Nombre="Lionel Messi", Carrera="Sistemas")
print(alumno1)
print(f"Antigüedad de {alumno1.datos['Nombre']}: {alumno1.antiguedad()} años")
print(f"¿Los alumnos tienen el mismo DNI?: {alumno1 == alumno2}")

#ejercicio3 y 4

from datetime import date
import random
import string

class Alumno:
    #crea el diccionario de datos del alumno
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }

    def cambiar_datos(self, **nuevos_datos):
        #permite actualizar datos del alumno
        for key, value in nuevos_datos.items():
            if key in self.datos:
                self.datos[key] = value
            else:
                print(f"Clave '{key}' no existe en los datos del alumno.")

    def antiguedad(self):
        #calcula la antiguedad de años desde la fecha de ingreso
        hoy = date.today()
        antiguedad = hoy.year - self.datos["FechaIngreso"].year - ((hoy.month, hoy.day) < (self.datos["FechaIngreso"].month, self.datos["FechaIngreso"].day))
        return antiguedad

    def __str__(self):
        return f"Alumno(Nombre: {self.datos['Nombre']}, DNI: {self.datos['DNI']}, FechaIngreso: {self.datos['FechaIngreso']}, Carrera: {self.datos['Carrera']})"

    def __eq__(self, otro):
        #compara si dos objetos "alumno" tiene el mismo DNI
        if isinstance(otro, Alumno):
            return self.datos["DNI"] == otro.datos["DNI"]
        return False

class Nodo:
    #representa un nodo en la lista doblemente enlazada, contiene un dato (objeto Alumno) y referencias a los nodos anterior y siguiente.
    def __init__(self, dato=None):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:  
    #administra la lista doblemente enlazada, permite agregar nodos y provee un iterador.
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def __iter__(self):
        return IteradorLista(self.cabeza)

    @staticmethod
    def lista_ejemplo():
        #genera una lista de alumnos con datos aleatorios.
        nombres = ['Felipe', 'Laura', 'Roberto', 'Maria', 'Carlos']
        carreras = ['Sistemas', 'Medicina', 'Derecho', 'Arquitectura', 'Economía']
        lista = ListaDoblementeEnlazada()

        for _ in range(5):
            nombre = random.choice(nombres) + " " + ''.join(random.choices(string.ascii_uppercase, k=5))
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = date(random.randint(2015, 2021), random.randint(1, 12), random.randint(1, 28))
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            lista.agregar(alumno)

        return lista

    def ordenar_por_fecha_ingreso(self):
        if not self.cabeza:
            return

        cambiado = True
        while cambiado:
            cambiado = False
            nodo_actual = self.cabeza
            while nodo_actual and nodo_actual.siguiente:
                if nodo_actual.dato.datos["FechaIngreso"] > nodo_actual.siguiente.dato.datos["FechaIngreso"]:
                    # Intercambiar datos de los nodos
                    nodo_actual.dato, nodo_actual.siguiente.dato = nodo_actual.siguiente.dato, nodo_actual.dato
                    cambiado = True
                nodo_actual = nodo_actual.siguiente

class IteradorLista:
    def __init__(self, nodo):
        self.nodo_actual = nodo

    def __iter__(self):
        return self

    def __next__(self):
        if not self.nodo_actual:
            raise StopIteration
        alumno = self.nodo_actual.dato
        self.nodo_actual = self.nodo_actual.siguiente
        return alumno

# Ejemplo de uso:
lista_alumnos = ListaDoblementeEnlazada.lista_ejemplo()
print("Lista antes de ordenar:")
for alumno in lista_alumnos:
    print(alumno)

lista_alumnos.ordenar_por_fecha_ingreso()

print("\nLista después de ordenar por fecha de ingreso:")
for alumno in lista_alumnos:
    print(alumno)


