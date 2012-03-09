#encoding: utf-8

def subcadeia_de_soma_maxima(cadeia):
  inicio_intervalo_soma_maxima, fim_intervalo_soma_maxima, total  = 0, 0, 0
  indices_cadeia = range(len(cadeia))

  for inicio in indices_cadeia:
    soma = cadeia[inicio]
    for fim in indices_cadeia[inicio:]:
      if inicio != fim:
        soma += cadeia[fim]

      if soma > total:
        total = soma
        inicio_intervalo_soma_maxima = inicio
        fim_intervalo_soma_maxima = fim

  return ([inicio_intervalo_soma_maxima, fim_intervalo_soma_maxima], total)
