#include <stdio.h>

int main(void)
{
    char name[50];
    
    printf("What's your name?: ");
    fgets(name, sizeof(name), stdin);

    printf("Hello, %s\n", name);

    return 0;
}