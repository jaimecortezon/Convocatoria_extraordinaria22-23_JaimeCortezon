def bolsa(objetos, capacidad):
    # ordena los objetos por relación valor/peso
    objetos = sorted(objetos, key=lambda x: x[1] / x[2], reverse=True)

    # inicializa variables para almacenar la capacidad y el valor de los objetos seleccionados
    total_valor = 0
    total_peso = 0
    selected_objetos = []

    # recorre la lista de objetos
    for objeto in objetos:
        if total_peso + objeto[2] <= capacidad:
            # si el objeto cabe completo, lo agrega a la mochila
            total_valor += objeto[1]
            total_peso += objeto[2]
            selected_objetos.append(objeto[0])
        else:
            # si el objeto no cabe completo, agrega una fracción del objeto
            remaining = capacidad - total_peso
            fraction = remaining / objeto[2]
            total_valor+= objeto[1] * fraction
            selected_objetos.append(objeto[0])
            break

    return total_valor, selected_objetos

# ejemplo de uso
objetos = [('pistola', 60, 10), ('espada', 100, 20), ('escudo', 120, 30)]
capacidad = 50
valor, seleccionados = bolsa(objetos, capacidad)
print("Valor: ", valor)
print("obejtos seleccionados: ", seleccionados)
