from manual_matrix_search import buscar_coordenadas_multiples

def test_busqueda_matriz():
    grid = [[1, 2, 3], [5, 6, 3], [9, 7, 3]]
    res = buscar_coordenadas_multiples(grid, [3, 6, 99])
    assert res[3] == [(0, 2), (1, 2), (2, 2)]
    assert res[6] == [(1, 1)]
    assert res[99] == []