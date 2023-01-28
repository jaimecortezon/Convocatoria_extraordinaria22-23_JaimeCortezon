import random
import string

class armaduras:
    def __init__(self, rango, nombre):
        self.rango = rango
        self.nombre = nombre
        self.legion = rango[:2]
        self.numero = rango[2:]


def generarlegion():
    legion = ["FL", "TF", "TK", "CT", "FN", "FO"]
    return random.choice(legion)

def generarnumero():
    numero = str(random.randint(1000,9999))
    return numero


def generarnombre():
    nombre = ""
    for i in range(0,4):
        nombre += random.choice(string.ascii_uppercase)
    return nombre

def crear_tropa():
    tropa = []
    for i in range(0,2000):
        legion = generarlegion()
        numero = generarnumero()
        nombre = generarnombre()
        rango = legion + numero
        armadura = armaduras(rango, nombre)
        tropa.append(armadura)
    return tropa




def agruparlegion(tropa):
    legiones = {}
    for i in tropa:
        legion = i.legion
        if legion in legiones:
            legiones[legion].append(i)
        else:
            legiones[legion] = [i]
    return legiones



def agruparnumero(tropa):
    numeros = {}
    for i in tropa:
        numero = i.numero
        if numero in numeros:
            numeros[numero].append(i)
        else:
            numeros[numero] = [i]
    return numeros



def desertor(tropa):
    for i in tropa:
        if i.rango == "FN-2187":
            print("La armadura FN-2187 está cargada")
            tropa.remove(i)
            print("La armadura FN-2187 ha sido eliminada")
        else:
            print("La armadura FN-2187 no está cargada")
    return tropa


def asignar_mision(tropa):
    mision = {}
    for i in tropa:
        if i.numero[-3:] == "781":
            mision["asalto"] = i
        elif i.numero[-3:] == "537":
            mision["exploracion"] = i
    return mision


def asignar_mision2(tropa):
    mision = {}
    for i in tropa:
        if i.legion == "CT":
            mision["custodia"] = i
        elif i.legion == "TF":
            mision["exterminacion"] = i
    return mision

tropa = crear_tropa()
tropa = desertor(tropa)
print(tropa)