#include<cmath>
using namespace std;

// daily_rate calculates the daily rate given an hourly rate
double daily_rate(const double& hourly_rate) {
    return (hourly_rate * 8);
}

// apply_discount calculates the price after a discount
double apply_discount(const double& before_discount, const double& discount) {
    return (before_discount * ((100 - discount) / 100));
}

// monthly_rate calculates the monthly rate, given an hourly rate and a discount
// The returned monthly rate is rounded up to the nearest integer.
int monthly_rate(double hourly_rate, double discount) {
    double monthly_rate = hourly_rate * 8 * 22;
    
    return ceil(monthly_rate * ((100 - discount) / 100));
}

// days_in_budget calculates the number of workdays given a budget, hourly rate,
// and discount The returned number of days is rounded down (take the floor) to
// the next integer.
int days_in_budget(int budget, double hourly_rate, double discount) {
    double after_discount_daily_rate = (hourly_rate * ((100 - discount) / 100) * 8);
    double days_covered = budget / after_discount_daily_rate;
    return floor(days_covered);
}
