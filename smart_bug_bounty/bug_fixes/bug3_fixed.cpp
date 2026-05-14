#include <iostream>
#include <string>
void reverseString(std::string& s) {
int n = s.length();
for (int i = 0; i < n / 2; i++) {
char temp = s[i];
s[i] = s[n - 1 - i];
s[n - 1 - i] = temp;
}
}
int main() {
std::string str = "Hello";
reverseString(str);
std::cout << str << std::endl;
return 0;
}
