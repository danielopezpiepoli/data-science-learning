def maximo_clientes_concurrencia(registro: str) -> int:
    actual = 0
    pico_maximo = 0
    for evento in registro.lower():
        if evento == "e":
            actual += 1
            if actual > pico_maximo:
                pico_maximo = actual
        elif evento == "s":
            actual = max(0, actual - 1)
    return pico_maximo


def racha_maxima_positiva(secuencia: str) -> int:
    racha_actual = 0
    record_racha = 0
    for balance in secuencia:
        if balance == "+":
            racha_actual += 1
            if racha_actual > record_racha:
                record_racha = racha_actual
        elif balance == "-":
            racha_actual = 0
    return record_racha