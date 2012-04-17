#include "quicksort.h"

int *quicksort(int *input, int length_of_input) {
  int pivot_position = length_of_input - 1; // taking the last number as pivot
  int *smaller, *greater, *sorted_smaller, *sorted_greater, *output, pivot[1];
  int len_of_smaller, len_of_greater;
  int i, j, k;

  if (length_of_input <= 1) {
    return input;
  }

  pivot[0] = input[pivot_position];

  output = malloc(length_of_input * sizeof(int));

  for (i=0; i <= length_of_input - 2; i++) {
    if (input[i] > input[pivot_position])
      len_of_greater++;
    else if (input[i] > input[pivot_position])
      len_of_smaller++;
  }

  smaller = malloc(len_of_smaller * sizeof(int));
  greater = malloc(len_of_greater * sizeof(int));
//  sorted_smaller = malloc(len_of_smaller * sizeof(int));
//  sorted_greater = malloc(len_of_greater * sizeof(int));


  for (i=0; i <= length_of_input - 2; i++) {
    if (input[i] > input[pivot_position]) {
      greater[j] = input[i];
      j++;
    }
    else if (input[i] > input[pivot_position]) {
      smaller[k] = input[i];
      k++;
    }
  }

//  sorted_smaller = quicksort(smaller, len_of_smaller);
//  sorted_greater = quicksort(greater, len_of_greater);

  memcpy((void *)output, (void *)sorted_smaller, len_of_smaller * sizeof(int));
  printf("Pia o output: "); for (i=0;i<length_of_input;i++) printf(" %d ", output[i]);printf("\n");

  memcpy((void *)(output + (len_of_smaller * sizeof(int))), (void *)pivot, 1 * sizeof(int));
  printf("Pia o output: "); for (i=0;i<length_of_input;i++) printf(" %d ", output[i]);printf("\n");

  memcpy((void *)(output + (len_of_smaller + 1 * sizeof(int))), (void *)sorted_greater, len_of_greater * sizeof(int));
  printf("Pia o output: "); for (i=0;i<length_of_input;i++) printf(" %d ", output[i]);printf("\n");

  return output;
}
