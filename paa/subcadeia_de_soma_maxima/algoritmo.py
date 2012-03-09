#encoding: utf-8

def subcadeia_de_soma_maxima(cadeia):
  inicio_intervalo_soma_maxima, fim_intervalo_soma_maxima, total  = 0, 0, 0
  indices_cadeia = range(len(cadeia))
  inicio, soma = 0, 0

  for fim in indices_cadeia:
    soma += cadeia[fim]

    if soma < 0:
      inicio = fim+1
      soma = 0

    if soma > total:
      total = soma
      inicio_intervalo_soma_maxima = inicio
      fim_intervalo_soma_maxima = fim

  return ([inicio_intervalo_soma_maxima, fim_intervalo_soma_maxima], total)
