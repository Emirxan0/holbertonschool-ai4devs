#include <iostream>
#include <vector>

/*
  Bu proqram massivdəki ən böyük ədədi tapmalıdır.
*/

int main() {
    int numbers[] = {12, 45, 7, 89, 34};
    int n = 5;
    
    // 1. Logic Error: Max dəyişəni çox böyük rəqəmlə başladılır
    int max_val = 999999; 

    for (int i = 0; i <= n; i++) {
        // 2. Runtime Error: Massiv sərhədlərindən kənara çıxma (Out of bounds)
        // numbers[5] mövcud deyil
        if (numbers[i] > max_val) {
            max_val = numbers[i];
        }
    }

    // 3. Syntax Error: Nöqtəli vergül unudulub
    std::cout << "Ən böyük ədəd: " << max_val << std::endl
    
    return 0;
}
