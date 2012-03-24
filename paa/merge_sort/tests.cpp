#include <iostream>
#include <vector>
#include "my_mergesort.h"

using namespace std;

template<class T> void assert_equal(T result, T expected) {
    if (result == expected)
        cout << "PASSED" << endl;
    else
        cout << "FAILED" << endl;
}

void test_send_array_of_ints_with_size_one_should_return_itself(void) {
    vector<int> array_of_length_one(1, 10);
    vector<int> expected(1, 10);

    assert_equal(expected, my_mergesort(array_of_length_one));
    assert_equal(expected[0], my_mergesort(array_of_length_one)[0]);
}

void test_unsorted_even_array_should_be_sorted(void) {
    int pinput[] = {8, 4, 2, 6};
    int pexpected[] = {2, 4, 6, 8};

    vector<int> input(pinput, pinput + sizeof(pinput) / sizeof(int));
    vector<int> expected(pexpected, pexpected + sizeof(pexpected) / sizeof(int));
    vector<int> output;

    output = my_mergesort(input);

    assert_equal(expected, output);
}

int main(void) {
    test_send_array_of_ints_with_size_one_should_return_itself();
    test_unsorted_even_array_should_be_sorted();
}
