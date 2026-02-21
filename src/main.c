#include <stdio.h>
#include <unistd.h>
#include "./clock.h"

#define MAX_HOUR    23
#define MAX_MINUTE 59
#define MAX_SECOND 59

#define TIME_STR_LEN 9

int hour;
int minute;
int second;
char time_str[TIME_STR_LEN];

int parse_time(const char *time_str, int *h, int *m, int *s) {
    return sscanf(time_str, "%d:%d:%d", h, m, s);
}

int validate_time(int h, int m, int s) {
    if (h >= 0 && h <= MAX_HOUR && m >= 0 && m <= MAX_MINUTE && s >= 0 && s <= MAX_SECOND) {
        return 1;
    }
    return 0;
}

void print_time(int h, int m, int s) {
    printf("\rHora actual: %02d:%02d:%02d", h, m, s);
    fflush(stdout);
}

int next_second(int s) {
    s++;
    if (s > MAX_SECOND) {
        return 0;
    }
    return s;
}

int next_minute(int m, int s) {
    if (s == 0) {
        m++;
        if (m > MAX_MINUTE) {
            return 0;
        }
    }
    return m;
}

int next_hour(int h, int m, int s) {
    if (m == 0 && s == 0) {
        h++;
        if (h > MAX_HOUR) {
            return 0;
        }
    }
    return h;
}

#ifndef UNIT_TEST
int main() {
    printf("Introduzca la hora en formato HH:MM:SS\n");
    scanf("%8s", time_str);

    int slices = parse_time(time_str, &hour, &minute, &second);

    if (slices != 3 || validate_time(hour, minute, second) == 0) {
        printf("Formato o valores inválidos\n");
        return 1;
    }

    while (1) {
        print_time(hour, minute, second);
        sleep(1);

        second = next_second(second);
        minute = next_minute(minute, second);
        hour = next_hour(hour, minute, second);
    }

    return 0;
}
#endif /* UNIT_TEST */
