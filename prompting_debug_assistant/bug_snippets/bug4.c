/*
 * Bug 4 - bug4.c
 * Intended Behavior: Reverse a C string in-place using two pointers
 *                    starting from both ends and swapping characters
 *                    until the pointers meet in the middle.
 *                    Should handle empty strings without crashing.
 * Issue Type: Off-by-one error + undefined behaviour on empty string.
 * Notes: strlen() returns size_t (unsigned). For empty string,
 *        strlen(str) - 1 wraps to SIZE_MAX causing crash or infinite loop.
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
