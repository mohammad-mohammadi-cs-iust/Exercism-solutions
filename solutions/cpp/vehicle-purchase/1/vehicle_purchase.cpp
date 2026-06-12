#include "vehicle_purchase.h"
#include<string>

namespace vehicle_purchase {
bool needs_license(std::string kind) {
    if(kind == "car" || kind == "truck")
        return true;
    return false;
}
    
std::string choose_vehicle(std::string option1, std::string option2) {
    if(option1.compare(option2) <= 0)
        return (option1 + " is clearly the better choice.");
    else if(option1.compare(option2) > 0)
        return (option2 + " is clearly the better choice.");
    return "not yet implemented";
}

double calculate_resell_price(double original_price, double age) {
    if(age < 3)
        return (original_price * 0.8);
    else if(age < 10)
        return (original_price * 0.7);
    else if(age >= 10)
        return (original_price * 0.5);
    
    return 0.0;
}

}
