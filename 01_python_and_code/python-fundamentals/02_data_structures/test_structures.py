from choir_resource_allocator import compilar_censo_coral, es_obra_representable

def test_censo_coral():
    cantantes = [("Maria", "soprano", True), ("Luciano", "tenor", False)]
    censo = compilar_censo_coral(cantantes)
    assert censo["soprano"] == [1, 1]
    assert censo["tenor"] == [1, 0]

def test_viabilidad_obra():
    censo = {'bajo': [7, 1], 'soprano': [15, 3], 'tenor': [9, 0], 'contralto': [10, 2]}
    assert es_obra_representable(censo, {'bajo': [2, 0], 'soprano': [4, 0]}) is True
    assert es_obra_representable(censo, {'tenor': [10, 0]}) is False