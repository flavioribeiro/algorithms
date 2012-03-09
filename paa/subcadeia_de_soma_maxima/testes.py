from algoritmo import subcadeia_de_soma_maxima

def test_subcadeia_de_soma_maxima_deve_retornar_posicoes_inicial_e_final_e_soma():
  cadeia = [1,2,3]
  assert ([0,2], 6) == subcadeia_de_soma_maxima(cadeia)

def test_subcadeia_de_soma_maxima_deve_buscar_pela_subcadeia_de_maior_soma():
  cadeia = [-2, 11, -4, 13, -5, -2] #exemplo da sala de aula
  assert ([1, 3], 20) == subcadeia_de_soma_maxima(cadeia) #indices diferentes do slide pq arrays em python comecam de 0
