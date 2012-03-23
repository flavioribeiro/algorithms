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

int main(void) {
    test_send_array_of_ints_with_size_one_should_return_itself();
}
