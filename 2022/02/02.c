#include <stdio.h>

int main() {
    FILE* file = fopen("input.txt", "r");
    int p1 = 0, p2 = 0;

    for (char o, j, y; fscanf(file, "%c%c%c%c", &o, &j, &y, &j) == 4; p2++) {
        p1 += (y - ++o) % 3 * 3 + y - 87;
        p2 += (y - 88) * 3 + (y + ++o) % 3;
    }

    printf("%d\n%d\n", p1, p2);
}

