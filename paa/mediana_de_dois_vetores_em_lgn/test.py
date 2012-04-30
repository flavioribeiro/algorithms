from mediana import acha_mediana

def test_mediana_de_dois_vetores_deve_retornar_mediana_em_lgn():
    vetor_1 = [2,4,5,8,10]
    vetor_2 = [1,3,12,13,14]

    n = len(vetor_1)

    assert 8 == acha_mediana(vetor_1, 0, len(vetor_1), vetor_2, n)

