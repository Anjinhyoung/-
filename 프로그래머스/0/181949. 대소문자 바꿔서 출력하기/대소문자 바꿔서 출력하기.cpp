#include <iostream>
#include <string>


int main(void) {
    std::string str;
    std::cin >> str;
    
    for(size_t order = 0; order < str.size(); order++){
        if(isupper(str[order])){
            
            str[order] = tolower(str[order]);
        } else{
            
            str[order] = toupper(str[order]);
        }
    }
    std::cout << str;
        
    return 0;
}