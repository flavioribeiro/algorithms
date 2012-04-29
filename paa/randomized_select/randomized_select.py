#encoding: utf-8
import random

def RANDOMIZED_PARTITION(vetor, p, r):
    ultima_posicao = r-1
    print "- Randomized Partition comecou:",  vetor, "Verificando de ", p,"ate", r
    pivot = vetor[ultima_posicao]
#    pivot = random.randrange(p, r)

    print "- Pivot escolhido", pivot
    i = p
    for j in range(p, ultima_posicao):
        if vetor[j] <= pivot:
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1
    vetor[i], vetor[ultima_posicao] = vetor[ultima_posicao], vetor[i]
    print "- Randomized Partition terminou:", vetor, " Retornando:", i
    return i

def RANDOMIZED_SELECT(vetor, posicao_inicial, posicao_final, i):
    print "RANDOMIZED_SELECT", vetor, posicao_inicial, posicao_final, i
    if posicao_final + 1 == posicao_inicial:
        return vetor[posicao_inicial]
    q = RANDOMIZED_PARTITION(vetor, posicao_inicial, posicao_final)
    k = q - posicao_inicial
    if i == k:
        print "O escolhido é o pivot"
        return vetor[q]
    elif i < k:
        print "[i %d < k %d]" %(i,k), vetor, posicao_inicial, q, i
        return RANDOMIZED_SELECT(vetor, posicao_inicial, q, i)

    else:
        print "[i %d > k %d]" %(i,k), vetor, q, posicao_final, i-k
        return RANDOMIZED_SELECT(vetor, q, posicao_final, i - k)


