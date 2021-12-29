#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool check_key(string s);
void cipher(string p, int key);

int main(int argc, string argv[])
{
    if (argc != 2 || !check_key(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);

    string p = get_string("plaintext: ");

    printf("ciphertext: ");

    cipher(p, key);
}

void cipher(string p, int key)
{
    for (int i = 0; i < strlen(p); i++)
    {
        char c = p[i];

        if (isalpha(c))
        {
            char m = 'A';

            if (islower(c))
            {
                m = 'a';
            }

            printf("%c", (c - m + key) % 26 + m);

        }

        else
        {
            printf("%c", c);
        }
    }
    printf("\n");
}

bool check_key(string s)
{
    for (int i = 0; i < strlen(s); i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }

    return true;
}
