def buscar_coordenadas_multiples(matriz: list, elementos_busqueda: list) -> dict:
    resultados = {elem: [] for elem in elementos_busqueda}
    if not matriz:
        return resultados
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            valor = matriz[i][j]
            if valor in resultados:
                resultados[valor].append((i, j))
    return resultados