#encoding: utf-8

def subcadeia_de_soma_maxima(cadeia):
  inicio_intervalo_soma_maxima, fim_intervalo_soma_maxima, soma  = 0, 0, 0
  indices_cadeia = range(len(cadeia))

  for inicio in indices_cadeia:
    for fim in indices_cadeia[inicio:]:

      if sum(cadeia[inicio:fim+1]) > soma:
        soma = sum(cadeia[inicio:fim+1])
        inicio_intervalo_soma_maxima = inicio
        fim_intervalo_soma_maxima = fim

  return ([inicio_intervalo_soma_maxima, fim_intervalo_soma_maxima], soma)
