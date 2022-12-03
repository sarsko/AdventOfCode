#include <stdio.h>
#include <stdlib.h>

int main() {
    char *source, src_orig;
    src_orig = source;
    FILE *fp = fopen("input.txt", "r");

    fseek(fp, 0L, SEEK_END);
    long bufsize = ftell(fp);

    source = malloc(sizeof(char) * (bufsize + 1));

    fseek(fp, 0L, SEEK_SET);
    fread(source, sizeof(char), bufsize, fp);

    fclose(fp);

    int p1 = 0, p2 = 0;
    for (;*source;p2++) {
        p1 += (2[source] - ++*source++) % 3 * 3 + *++source - 87;
        p2 += (*source - 88) * 3 + (*source++ + ++source++[-3]) % 3;
    }
    printf("%d\n%d\n", p1, p2);

    free(src_orig);

    FILE* file = fopen("input.txt", "r");
    p1 = 0, p2 = 0;

    for (char o, j, y; fscanf(file, "%c%c%c%c", &o, &j, &y, &j) == 4; p2++) {
        p1 += (y - ++o) % 3 * 3 + y - 87;
        p2 += (y - 88) * 3 + (y + ++o) % 3;
    }

    printf("%d\n%d\n", p1, p2);
}

