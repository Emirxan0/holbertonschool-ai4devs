/*
 * Bug 4 - bug4_fixed.c
 * Fix: Added NULL and empty-string guard. Cast strlen() to int.
 */

#include <stdio.h>
#include <string.h>
#include <assert.h>

void reverse_string(char *str) {
    if (str == NULL || str[0] == '\0')
        return;
    int left = 0;
    int right = (int)strlen(str) - 1;
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
    char word4[] = "a";
    reverse_string(word1);
    assert(strcmp(word1, "olleh") == 0);
    printf("Reversed: %s\n", word1);
    reverse_string(word2);
    assert(strcmp(word2, "") == 0);
    printf("Reversed: '%s'\n", word2);
    reverse_string(word3);
    assert(strcmp(word3, "edcba") == 0);
    printf("Reversed: %s\n", word3);
    reverse_string(word4);
    assert(strcmp(word4, "a") == 0);
    printf("Reversed: %s\n", word4);
    printf("All tests passed!\n");
    return 0;
}
