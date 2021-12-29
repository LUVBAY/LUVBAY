#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    int cents = 0;
    float amount;

    do
    {
        amount = get_float("Change owed: ");
    }
    while (amount < 0);
    {
        cents = round(amount * 100);


        int count = 0, amount_left = cents;
        count += amount_left / 25, amount_left %= 25;
        count += amount_left / 10, amount_left %= 10;
        count += amount_left / 5, amount_left %= 5;
        count += amount_left;

        printf("%i\n", count);


    }
}
