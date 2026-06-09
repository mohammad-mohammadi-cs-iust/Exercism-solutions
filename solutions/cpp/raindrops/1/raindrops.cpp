#include "raindrops.h"
#include<string>
#include<iostream>
using namespace std;

namespace raindrops {
    string convert(const int &num){
        string s = "";
        if(num % 3 == 0)
            s.insert(s.size(), "Pling");
        if(num % 5 == 0)
            s.insert(s.size(), "Plang");
        if(num % 7 == 0)
            s.insert(s.size(), "Plong");
       
        
        if(s.empty()){
             string Snum = to_string(num);
            return Snum;
        }
        return s;
    }    

}  // namespace raindrops
