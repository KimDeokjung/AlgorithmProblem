#include <stdio.h>
#include <string.h>

int main()
{
    int t;
    scanf("%d", &t);
    char *result[t];

    for (int i = 0; i < t; i++) {
        char str[25];
        int tmp;
        scanf("%s", str);

        tmp = strlen(str);
        if (6 <= tmp && tmp <= 9) {
            result[i] = "yes";
        }else{
            result[i] = "no";
        }
    } 

    for (int i = 0; i < t; i++) {
        printf("%s\n", result[i]);
    }

    return 0;
}