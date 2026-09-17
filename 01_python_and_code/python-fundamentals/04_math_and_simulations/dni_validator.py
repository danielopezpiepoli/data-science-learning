def validar_dni(dni: str) -> bool:
    """
    Valida un DNI espanol verificando longitud (9 caracteres),
    8 digitos numericos y coincidencia de la letra segun modulo 23.
    """
    codigo_control = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    if len(dni) != 9:
        return False
        
    num_str, letra = dni[:8], dni[-1].upper()
    
    if not num_str.isdigit():
        return False
        
    numero = int(num_str)
    return letra == codigo_control[numero % 23]


def filtrar_dnis_invalidos(lista_dnis: list) -> list:
    """Devuelve la lista con los DNIs que no superan la validacion."""
    return [dni for dni in lista_dnis if not validar_dni(dni)]