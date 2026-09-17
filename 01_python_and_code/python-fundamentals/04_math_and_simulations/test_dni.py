from dni_validator import validar_dni, filtrar_dnis_invalidos

def test_dni_valido():
    assert validar_dni("12345678Z") is True
    assert validar_dni("00000000T") is True

def test_dni_invalido_letra():
    assert validar_dni("12345678A") is False

def test_dni_invalido_formato():
    assert validar_dni("123A5678Z") is False
    assert validar_dni("12345") is False
    assert validar_dni("1234567890Z") is False

def test_filtrar_dnis_invalidos():
    lista = ["12345678Z", "00000000T", "14879544S"]
    assert filtrar_dnis_invalidos(lista) == ["14879544S"]