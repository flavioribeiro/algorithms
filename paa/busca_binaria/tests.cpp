#include <iostream>
#include <vector>
#include "binary_search.h"

using namespace std;

template<class T> void assert_equal(T result, T expected) {
    if (result == expected)
        cout << "PASSED" << endl;
    else
        cout << "FAILED" << endl;
}


void test_search_for_a_number_in_array_should_return_it_position(void) {
    int pinput[] = {0, 1, 2, 3, 4, 5, 6, 7};
    int output;
    vector<int> input(pinput, pinput + sizeof(pinput) / sizeof(int));

    output = binary_search(input, 2);

    assert_equal(output, 2);
}

void test_search_for_a_number_in_array_of_odd_numbers_should_return_it_position(void) {
    int pinput[] = {1, 3, 5, 7, 9, 11, 13, 15};
    int output;
    vector<int> input(pinput, pinput + sizeof(pinput) / sizeof(int));

    output = binary_search(input, 7);

    assert_equal(output, 3);
}


int main(void) {
    test_search_for_a_number_in_array_should_return_it_position();
    test_search_for_a_number_in_array_of_odd_numbers_should_return_it_position();
}
