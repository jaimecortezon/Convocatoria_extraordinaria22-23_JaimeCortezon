import datetime

class Artefactosvaliosos:
    def __init__(self, nombre: str, peso: float, precio: float, fecha_caducidad: str):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
        self.fecha_caducidad = datetime.datetime.strptime(fecha_caducidad, '%d-%m-%Y')
        
    def __str__(self):
        return f"Artefactosvaliosos: {self.nombre} {self.peso} {self.precio} {self.fecha_caducidad}"
    
    def set_nombre(self, nombre: str):
        self.nombre = nombre
        
    def set_peso(self, peso: float):
        if peso < 0:
            raise ValueError("El peso no puede ser negativo")
        self.peso = peso
        
    def set_precio(self, precio: float):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = precio
        
    def set_fecha_caducidad(self, fecha_caducidad: str):
        self.fecha_caducidad = datetime.datetime.strptime(fecha_caducidad, '%d-%m-%Y')
        
   
    def create_artefactosvaliosos(num: int):
        mochila = []
        for i in range(num):
            nombre = input("Nombre del artefacto: ")
            peso = float(input("Peso del artefacto: "))
            precio = float(input("Precio del artefacto: "))
            fecha_caducidad = input("Fecha de caducidad del artefacto (dd-mm-yyyy): ")
            artefacto = Artefactosvaliosos(nombre, peso, precio, fecha_caducidad)
            mochila.append(artefacto)
        return mochila
    

    def sort_by_fecha_caducidad(mochila: list):
        mochila.sort(key=lambda x: x.fecha_caducidad)
    
    def modificarvalor(artefacto):
        artefacto.precio = input("Nuevo precio del artefacto: ")
        return artefacto
    
    
if __name__=="__main__":
    artefactos = Artefactosvaliosos.create_artefactosvaliosos(2)
    Artefactosvaliosos.sort_by_fecha_caducidad(artefactos)
    
    for artefacto in artefactos:
        print(artefacto)

