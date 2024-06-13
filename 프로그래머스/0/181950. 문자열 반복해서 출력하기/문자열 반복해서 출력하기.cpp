#include <iostream>
#include <string>


int main(void) {
    std::string str;
    int n;
    std::cin >> str >> n;
    
    for(size_t order = 0;  order < n; order++){
        std::cout << str; 
    }
    
    return 0;
}