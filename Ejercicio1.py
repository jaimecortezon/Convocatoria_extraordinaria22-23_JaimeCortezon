class armaduras:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print(f'Armadura {nombre} de nivel {rango} creado con éxito.')
    
    def calificacion(self):
        if self.rango == 'MK':
            return 'bajo'
        elif self.rango == 'MP':
            return 'medio'
        elif self.rango == 'MA':
            return 'alto'
        else:
            return 'desconocido'

    def __str__(self):
        return f'{self.nombre} es una armadura tipo {self.calificacion()}'

def calificar_armaduras(armaduras_list):
    armaduras_levels = {}
    for armaduras in armaduras_list:
        level = armaduras.calificacion()
        if level in armaduras_levels:
            armaduras_levels[level] += 1
        else:
            armaduras_levels[level] = 1
    return armaduras_levels

def print_armaduras(armaduras_list):
    for armaduras in armaduras_list:
        print(armaduras)

armaduras_list = [armaduras('MK-7348', 'MK'), armaduras('MK-5498', 'MP'), armaduras('MK-8739', 'MA'), armaduras('MK-2893', 'AA')]
print_armaduras(armaduras_list)
print(calificar_armaduras(armaduras_list))
