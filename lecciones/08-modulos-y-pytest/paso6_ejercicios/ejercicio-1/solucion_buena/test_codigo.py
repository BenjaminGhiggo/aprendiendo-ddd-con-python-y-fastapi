from codigo import es_par

def test_par():
    assert es_par(4) is True

def test_impar():
    assert es_par(7) is False
