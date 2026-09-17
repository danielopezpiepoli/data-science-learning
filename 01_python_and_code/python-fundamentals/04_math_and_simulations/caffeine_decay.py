def tiempo_desintegracion_cafeina(tazas: int, umbral_mg: float = 10.0, mg_por_taza: float = 98.0) -> int:
    cafeina = tazas * mg_por_taza
    horas = 0
    while cafeina > umbral_mg:
        cafeina /= 2.0
        horas += 5
    return horas