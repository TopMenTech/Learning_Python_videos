#include <stdio.h>
#include <math.h>

int main()
{
    double base, exponent, result;

    base = 2.0;
    exponent = 4.0;

    result = pow(base, exponent);

    printf("%.2lf", result);

    return 0;
}
