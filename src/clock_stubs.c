#include "clock.h"
#include <stdio.h>

__attribute__((weak)) int parse_time(const char *time_str, int *h, int *m, int *s) {
    return -1; // stub: no implementado
}

__attribute__((weak)) int validate_time(int h, int m, int s) {
    return -1; // stub
}

__attribute__((weak)) void print_time(int h, int m, int s) {
    printf("[STUB] print_time called\n");
}

__attribute__((weak)) int next_second(int s) { return -1; }
__attribute__((weak)) int next_minute(int m, int s) { return -1; }
__attribute__((weak)) int next_hour(int h, int m, int s) { return -1; }