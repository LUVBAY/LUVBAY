#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int j, k, l, m, n;

    // prompt for start size
    do
    {
        m = get_int("Start size: ");

    }
    while (m < 9);

    // prompt for End size
    do
    {
        n = get_int("End size: ");
    }

    while (n < m);

    // Calculate number of years until we reach threshold
    for (j = 0; m < n; j++)
    {
        k = m / 3;
        l = m / 4;
        m = m + k - l;
    }

    // print number of years
    {
        printf("Years: %i\n", j);
    }
}
