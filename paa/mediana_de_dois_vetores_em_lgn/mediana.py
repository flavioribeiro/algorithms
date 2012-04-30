#!/usr/sbin/env python
#encoding: utf-8

import random

def acha_mediana(vetor_1, pos_inicial, pos_final, vetor_2, n):
    pos_mediana = n
    print "- A posição da mediana: ", n
    print "-- Buscando entre as posicoes %d e %d do vetor" % (pos_inicial, pos_final-1)

    pos_candidato = random.randrange(pos_inicial, pos_final)
    print "- A posicao do candidato: %d e o candidato: %d" % (pos_candidato, vetor_1[pos_candidato])

    menores_pos_candidato = pos_candidato - 1 #os de vetor1 que sao menores que candidato
    print "- Garantido como menores do candidato: ", vetor_1[:pos_candidato]

    faltam = pos_mediana - len(vetor_1[:pos_candidato])
    print "- Faltam: ", faltam

    for i in range(0, faltam):
        if vetor_2[i] > vetor_1[pos_candidato]: #o candidato ta mt pequeno
            print "- O candidato está muito pequeno ", vetor_2[i], vetor_1[pos_candidato]
            return acha_mediana(vetor_1, pos_candidato, pos_final, vetor_2, n)

    if vetor_2[i+1] > vetor_1[pos_candidato]:
        print "Comparando ", vetor_2[i+1], vetor_1[pos_candidato]
        print "Achado! ", vetor_1[pos_candidato]
        return vetor_1[pos_candidato]

    else:
        return acha_mediana(vetor_1, 0, pos_candidato+1, vetor_2, n)
