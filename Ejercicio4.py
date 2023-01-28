def hijo_sin_amor(mochila, objetos_sacados=0):
    if not mochila:
        return (False, objetos_sacados)
    objeto = mochila.pop(0)
    if objeto == "anillo de poder":
        return (True, objetos_sacados)
    else:
        objetos_sacados += 1
        return hijo_sin_amor(mochila, objetos_sacados)

# Ejemplo de uso
mochila = ["mjolnir", "guantelete de thanos", "anillo de poder", "vibranium"]
encontrado, objetos_sacados = hijo_sin_amor(mochila)
if encontrado:
    print(f"Se encontró el anillo de poder después de sacar {objetos_sacados} objetos.")
else:
    print("No se encontró el anillo de poder.")