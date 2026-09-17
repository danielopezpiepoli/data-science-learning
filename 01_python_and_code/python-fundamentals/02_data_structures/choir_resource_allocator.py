def compilar_censo_coral(cantantes: list) -> dict:
    censo = {
        "soprano": [0, 0],
        "contralto": [0, 0],
        "tenor": [0, 0],
        "bajo": [0, 0]
    }
    for _, voz, es_solista in cantantes:
        if voz in censo:
            censo[voz][0] += 1
            if es_solista:
                censo[voz][1] += 1
    return censo


def es_obra_representable(censo_disponible: dict, requisitos_obra: dict) -> bool:
    for cuerda, (req_total, req_solistas) in requisitos_obra.items():
        if cuerda not in censo_disponible:
            return False
        disp_total, disp_solistas = censo_disponible[cuerda]
        if req_total > disp_total or req_solistas > disp_solistas:
            return False
    return True