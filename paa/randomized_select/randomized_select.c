#include<stdio.h>
#include<stdlib.h>

void troca(int *x, int *y);
int  partition(int v[], int p, int r);
int  randomized_partition(int v[], int p, int r);
int  randomized_select(int v[], int p, int r, int i);
void imprime_vetor(int v[]);

int main() {
//    int vetor[] = {30,35,20,10,40,50,80,100}, i;
    int i;
    int vetor[] = {4, 6, 2, 3, 1, 8};

    printf("terceiro menor: %d\n", randomized_select(vetor, 0, 5, 1));
//    printf("segundo menor: %d\n", randomized_select(vetor, 0, 7, 2));

    return 0;
}

void troca(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

int partition(int vetor[], int posicao_inicial, int posicao_final) {
    int pivot = vetor[posicao_final]; // pegando sempre o pivot como ultimo elemento do array
    int i, j;

    printf("--- Entrando no partition: "); imprime_vetor(vetor);

    i = posicao_inicial - 1;

    for(j=posicao_inicial; j <= posicao_final-1; j++) {
        if(vetor[j] <= pivot) {
            i++;
            troca(&vetor[i], &vetor[j]);
        }
    }
    troca(&vetor[i+1], &vetor[posicao_final]);
    printf("--- Saindo do partition com quantidade de numeros até o pivot (%d): ", i+1); imprime_vetor(vetor);
    return i+1;
}

int randomized_partition(int vetor[], int posicao_inicial, int posicao_final) {
    int posicao_aleatoria = rand()/(RAND_MAX/posicao_final);
    printf("Randomized_partition: posicao aleatória: %d, Pivot: %d\n", posicao_aleatoria, vetor[posicao_aleatoria]);
    troca(&vetor[posicao_final], &vetor[posicao_aleatoria]);
    return partition(vetor, posicao_inicial, posicao_final);
}

void imprime_vetor(int vetor[]) {
    int i;
    printf("[");
    for (i=0; i< 5; i++) {
        printf(" %d ", vetor[i]);
    }
    printf("]\n");
}

int randomized_select(int vetor[], int posicao_inicial, int posicao_final, int i) { //i é o i-ésimo menor
    printf("Entrando no randomized_select (posicao_inicial=%d, posicao_final=%d, o que eu quero=%d):", posicao_inicial, posicao_final, i); imprime_vetor(vetor);

    if(posicao_inicial == posicao_final)
        return vetor[posicao_inicial];

    int q = randomized_partition(vetor, posicao_inicial, posicao_final);
    int k = q - posicao_inicial + 1;
    printf("q = %d\n", q);

    if(i == k) {
        printf("O que eu quero é igual o pivot!\n");
        return vetor[q];
    } else if (i < k) {
        printf("O que eu quero tá no pedaco menor, pq o i é menor que o pivot\n");
        return randomized_select(vetor, posicao_inicial, posicao_final-1, i);
    } else {
        printf("O que eu quero tá no pedaço maior, pq o i é maior que o pivot\n");
        return randomized_select(vetor, q+1, posicao_final, i-k);
    }
}
