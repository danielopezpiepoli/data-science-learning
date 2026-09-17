from time_series_streaks import maximo_clientes_concurrencia, racha_maxima_positiva

def test_maximo_clientes():
    assert maximo_clientes_concurrencia("eeseeessss") == 4
    assert maximo_clientes_concurrencia("eess") == 2

def test_racha_positiva():
    assert racha_maxima_positiva("+-++---++++") == 4
    assert racha_maxima_positiva("---") == 0