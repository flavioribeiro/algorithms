// merge sort
#include "my_mergesort.h"

vector<int> my_mergesort(vector<int> input) {
    int middle = (input.size() -1) / 2;
    vector<int> left_subarray;
    vector<int> right_subarray;
    vector<int> ordered_left_subarray;
    vector<int> ordered_right_subarray;
    vector<int> output;

    if (input.size() > 1) {
        for (int i=0;i <= (input.size() - 1);i++) {
            if (i <= middle) {
                left_subarray.push_back(input[i]);
            } else {
                right_subarray.push_back(input[i]);
            }
        }

        ordered_left_subarray = my_mergesort(left_subarray);
        ordered_right_subarray = my_mergesort(right_subarray);

        output = combine(ordered_left_subarray, ordered_right_subarray);

        return output;
    } else {
        return input;
    }
}

vector<int> combine(vector<int> left_subarray, vector<int> right_subarray) {
    int left_subarray_position = 0, right_subarray_position = 0;
    vector<int> output;
    int size_of_arrays = left_subarray.size();
    int big_int = 1000000000;

    left_subarray.push_back(big_int);
    right_subarray.push_back(big_int);

    for (int i=0; i <= (size_of_arrays) * 2; i++) {

        if (left_subarray[left_subarray_position] == big_int && right_subarray[right_subarray_position] == big_int) {
            //do nothing :P
        } else if (left_subarray[left_subarray_position] < right_subarray[right_subarray_position]) {
            output.push_back(left_subarray[left_subarray_position]);
            left_subarray_position++;

        } else {
            output.push_back(right_subarray[right_subarray_position]);
            right_subarray_position++;
        }
    }
    return output;
}
