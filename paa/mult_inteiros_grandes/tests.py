from mult import mult

def test_mult_inteiros_grandes_para_inteiros_menores_que_max_int():
    n_1 = 2101
    n_2 = 1130

    assert 2374130 == mult(n_1, n_2)
