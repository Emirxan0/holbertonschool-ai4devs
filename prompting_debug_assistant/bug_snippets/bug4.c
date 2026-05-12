/*
 * Bug 4 - bug4.c
 * Intended Behavior: Reverse a C string in-place using two pointers
 *                    starting from both ends, swapping characters until
 *                    the pointers meet in the middle. The function must
 *                    handle empty strings gracefully without crashing
 *                    or entering an infinite loop.
 * Issue Type: Off-by-one error and undefined behaviour on empty string.
 * Notes: strlen() returns size_t which is unsigned. For an empty string,
 *        strlen(str) minus 1 wraps to SIZE_MAX due to unsigned underflow.
 *        This causes out-of-bounds writes, a segfault, or infinite loop.
 */

#include <stdio.h>
#include <string.h>

void reverse_string(char *str) {
    int left = 0;
    int right = strlen(str) - 1;
    while (left < right) {
        char tmp  = str[left];
        str[left] = str[right];
        str[right] = tmp;
        left++;
        right--;
    }
}

int main(void) {
    char word1[] = "hello";
    char word2[] = "";
    char word3[] = "abcde";
    reverse_string(word1);
    printf("Reversed: %s\n", word1);
    reverse_string(word2);
    printf("Reversed: %s\n", word2);
    reverse_string(word3);
    printf("Reversed: %s\n", word3);
    return 0;
}
