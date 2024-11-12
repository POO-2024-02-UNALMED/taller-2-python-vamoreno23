class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, nuevoColor):
        col = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        if nuevoColor in col:
            self.color = nuevoColor 
class Motor:
    TIPOS_POSIBLES = ["electrico", "gasolina"]

    def __init__(self, numeroCilindros: int, tipo: str, registro: int) -> None
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro: int) -> None:
        self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo: str) -> None:
        //Asigna un nuevo tipo de motor 
        if nuevoTipo in self.TIPOS_POSIBLES:
            self.tipo = nuevoTipo

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1
    
    def cantidadAsientos(self):
        contador = 0
        for asiento in self.asientos:
            if asiento != None:
                contador += 1
        return contador

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            print(1)
            return "Las piezas no son originales"
        
        for asiento in self.asientos:
            if asiento is not None:
                if asiento.registro != self.registro:
                    print(3)
                    return "Las piezas no son originales"
            
        return "Auto original"