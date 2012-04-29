import random

def RANDOMIZED_PARTITION(vetor, p, r):
    print "Randomized Partition comecou:",  vetor
#    pivot = vetor[random.randrange(p, r-1)]
    pivot = vetor[r-1]
    print "- Pivot escolhido", pivot
    i = p
    for j in range(p, r-1):
        if vetor[j] <= pivot:
            vetor[i], vetor[j] = vetor[j], vetor[i]
            i += 1
    vetor[i], vetor[r-1] = vetor[r-1], vetor[i]
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


