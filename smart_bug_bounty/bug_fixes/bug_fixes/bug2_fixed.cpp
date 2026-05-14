#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {10, 20, 30};
    for (int i = 0; i < numbers.size(); i++) {
        std::cout << numbers[i] << std::endl;
    }
    return 0;
}
