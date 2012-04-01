#include "binary_search.h"

int position;

int binary_search(vector<int> input, int number) {
    int first, last;
    int middle = input.size() / 2;

    if (number < input[middle]) {
        vector<int> subvector(input.begin(), input.begin() + middle);
        return binary_search(subvector, number);
    } else if (number > input[middle]) {
        vector<int> subvector(input.begin() + middle, input.end());
        position = position + subvector.size();
        return binary_search(subvector, number);
    } else {
        return position + middle;
    }
}
