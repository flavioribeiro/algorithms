#include <check.h>
#include <stdlib.h>
#include <stdbool.h>
#include "../src/quicksort.h"

START_TEST (test_quicksort_should_return_array_of_int_ordered)
{
  int input[4] = {1, 2, 3, 4};
  int expected[4] = {1, 2, 3, 4};
  int *output;
  int i;

  output = malloc(4 * sizeof(int));
  memcpy((void *)output, (void *)quicksort(input, 4), 4 * sizeof(int));

  for (i=0; i < 4; i++) {
    fail_if(expected[i] != output[i], "Should have been sorted");
  }

  free(output);
}
END_TEST


Suite *video_geolocation_suite(void) {
    Suite *s = suite_create("video_geolocation");

    TCase *tc_core = tcase_create("Core");
    tcase_add_test(tc_core, test_quicksort_should_return_array_of_int_ordered);

    suite_add_tcase(s, tc_core);
    return s;
}

int main(void) {
    int number_failed;
    Suite *s = video_geolocation_suite();
    SRunner *sr = srunner_create(s);
    srunner_run_all(sr, CK_VERBOSE);
    number_failed = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (number_failed == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
}
