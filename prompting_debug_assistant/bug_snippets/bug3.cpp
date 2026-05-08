#include <iostream>
int main() {
    int numbers[] = {12, 45, 7, 89, 34};
    int n = 5;
    int max_val = 999999; 

    for (int i = 0; i <= n; i++) {
        if (numbers[i] > max_val) {
            max_val = numbers[i];
        }
    }

    std::cout << "Max: " << max_val << std::endl
    return 0;
}
