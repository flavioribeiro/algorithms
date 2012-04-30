#!/usr/sbin/env python
#encoding: utf-8

import random

def acha_mediana(vetor_1, pos_inicial, pos_final, vetor_2, n):
    pos_mediana = n
    print "-- Buscando entre as posicoes %d e %d do vetor" % (pos_inicial, pos_final-1)

    pos_candidato = (pos_final + pos_inicial) / 2
    print "- A posicao do candidato: %d e o candidato: %d" % (pos_candidato, vetor_1[pos_candidato])

    menores_pos_candidato = pos_candidato - 1 #os de vetor1 que sao menores que candidato
    print "- Garantido como menores do candidato: ", vetor_1[:pos_candidato]

    faltam = pos_mediana - len(vetor_1[:pos_candidato])
    print "- Faltam: ", faltam

    if vetor_2[faltam-1] > vetor_1[pos_candidato]:
        print "- O candidato está muito pequeno ", vetor_2[faltam-1], vetor_1[pos_candidato]
        return acha_mediana(vetor_1, pos_candidato+1, pos_final, vetor_2, n)

    if vetor_2[faltam] < vetor_1[pos_candidato]:
        print "- O candidato está muito grande", vetor_2[faltam+1], vetor_1[pos_candidato]
        return acha_mediana(vetor_1, pos_inicial, pos_candidato, vetor_2, n)

    if vetor_2[faltam] > vetor_1[pos_candidato] and vetor_2[faltam-1] < vetor_1[pos_candidato]:
        print "vetor_2[faltam+1]", vetor_2[faltam]
        print "vetor_2[faltam]", vetor_2[faltam-1]

        print "Achado! ", vetor_1[pos_candidato]
        return vetor_1[pos_candidato]
