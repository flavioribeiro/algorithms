#include<stdio.h>
#include<stdlib.h>

void troca(int *x, int *y);
int  partition(int v[], int p, int r);
int  randomized_partition(int v[], int p, int r);
int  randomized_select(int v[], int p, int r, int i);

void main() {
    int vetor[] = {30,35,20,10,40,50,80,100}, i;
    i = randomized_select(vetor, 0, 7, 3);

    printf("%d \n", i);
}

void troca(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

int partition(int vetor[], int posicao_inicial, int posicao_final) {
    int pivot = vetor[posicao_final];
    int i = posicao_inicial-1, j;

    for(j=posicao_inicial; j <= posicao_final-1; j++) {
        if(vetor[j] <= pivot) {
            i++;
            troca(&vetor[i], &vetor[j]);
        }
    }
    troca(&vetor[i+1], &vetor[posicao_final]);
    return i+1;
}

int randomized_partition(int vetor[], int posicao_inicial, int posicao_final) {
    int posicao_aleatoria = rand()/(RAND_MAX/posicao_final);
    troca(&vetor[posicao_final], &vetor[posicao_aleatoria]);
    return partition(vetor, posicao_inicial, posicao_final);
}

int randomized_select(int vetor[], int posicao_inicial, int posicao_final, int i) {
    if(posicao_inicial == posicao_final)
        return vetor[posicao_inicial];

    int q = randomized_partition(vetor, posicao_inicial, posicao_final);
    int k = q - posicao_inicial + 1;

    if(i == k)  //o pivo eh a resposta
        return vetor[q];
    else if (i < k)
        return randomized_select(vetor, posicao_inicial, posicao_final-1, i);
    else
        return randomized_select(vetor, q+1, posicao_final, i-k);
}
