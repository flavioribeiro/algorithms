import random

def RANDOMIZED_PARTITION(vetor, p, r):
    ultima_posicao = r-1
    print "Randomized Partition comecou:",  vetor
#    pivot = vetor[random.randrange(p, r-1)]
    pivot = vetor[ultima_posicao]
    print "- Pivot escolhido", pivot
    i = p
    for j in range(p, ultima_posicao):
        if vetor[j] <= pivot:
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1
    vetor[i], vetor[ultima_posicao] = vetor[ultima_posicao], vetor[i]
    print "Randomized Partition terminou:", vetor
    return i

def RANDOMIZED_SELECT(vetor, posicao_inicial, posicao_final, i):
    if posicao_final + 1 == posicao_inicial:
        return vetor[posicao_inicial]
    q = RANDOMIZED_PARTITION(vetor, posicao_inicial, posicao_final)
    k = q - posicao_inicial
    if i == k:
        return vetor[q]
    elif i < k:
        return RANDOMIZED_SELECT(vetor, posicao_inicial, q, i)
    return RANDOMIZED_SELECT(vetor, q, posicao_final, i - k)


