#include <stdio.h>
#include <string.h>

int main()
{
    int t, s;
    scanf("%d %d", &t, &s);

    if (s == 0 && 12 <= t && t <= 16) {
        printf("320");
    }else {
        printf("280");
    }


    return 0;
}