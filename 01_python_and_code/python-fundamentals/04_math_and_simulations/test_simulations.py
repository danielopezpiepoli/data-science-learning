from caffeine_decay import tiempo_desintegracion_cafeina

def test_cafeina():
    assert tiempo_desintegracion_cafeina(1) == 20
    assert tiempo_desintegracion_cafeina(6) == 30