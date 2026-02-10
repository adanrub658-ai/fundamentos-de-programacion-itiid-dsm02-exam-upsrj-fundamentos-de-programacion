#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <unistd.h> 
#include <fcntl.h>    
#include "../src/clock.h"

/* Colores */
#define GREEN "\033[92m"
#define RED   "\033[91m"
#define GRAY  "\033[90m"
#define RESET "\033[0m"

/* --- Helper para capturar stdout --- */
static int capture_print_time_output(char *buf, size_t size) {
    FILE *tmp = tmpfile();   // archivo temporal
    if (!tmp) return -1;

    // Redirigimos stdout
    int fd = dup(fileno(stdout));
    fflush(stdout);
    dup2(fileno(tmp), fileno(stdout));

    // Ejecutamos la función
    print_time(9,5,3);

    // Restauramos stdout
    fflush(stdout);
    dup2(fd, fileno(stdout));
    close(fd);

    // Leemos lo que se imprimió
    rewind(tmp);
    size_t n = fread(buf, 1, size-1, tmp);
    buf[n] = '\0';
    fclose(tmp);
    return 0;
}

/* --- Tests unitarios --- */

static void test_parse_time(void) {
    int h, m, s;
    int ret = parse_time("12:34:56", &h, &m, &s);
    if (ret == -1) {
        printf(RED "[FAIL]" RESET " parse_time() not implemented\n");
        return;
    }
    assert(ret == 3);
    assert(h == 12 && m == 34 && s == 56);
    printf(GREEN "[PASS]" RESET " parse_time()\n");
}

static void test_validate_time(void) {
    int ok = validate_time(23,59,59);
    if (ok == -1) {
        printf(RED "[FAIL]" RESET " validate_time() not implemented\n");
        return;
    }
    assert(ok == 1);
    assert(validate_time(24,0,0) == 0);
    printf(GREEN "[PASS]" RESET " validate_time()\n");
}

static void test_print_time(void) {
    char buffer[128];
    if (capture_print_time_output(buffer, sizeof(buffer)) != 0) {
        printf(RED "[FAIL]" RESET " print_time() capture error\n");
        return;
    }

    if (strstr(buffer, "[STUB]") != NULL) {
        printf(RED "[FAIL]" RESET " print_time() not implemented\n");
        return;
    }

    if (strstr(buffer, "Hora actual:") == NULL) {
        printf(RED "[FAIL]" RESET " print_time() wrong format\n");
        return;
    }

    printf(GREEN "[PASS]" RESET " print_time()\n");
}

static void test_next_second(void) {
    int val = next_second(59);
    if (val == -1) {
        printf(RED "[FAIL]" RESET " next_second() not implemented\n");
        return;
    }
    assert(val == 0);
    printf(GREEN "[PASS]" RESET " next_second()\n");
}

static void test_next_minute(void) {
    int val = next_minute(59,0);
    if (val == -1) {
        printf(RED "[FAIL]" RESET " next_minute() not implemented\n");
        return;
    }
    assert(val == 0);
    printf(GREEN "[PASS]" RESET " next_minute()\n");
}

static void test_next_hour(void) {
    int val = next_hour(23,0,0);
    if (val == -1) {
        printf(RED "[FAIL]" RESET " next_hour() not implemented\n");
        return;
    }
    assert(val == 0);
    printf(GREEN "[PASS]" RESET " next_hour()\n");
}

/* --- Main del tester --- */
int main(void) {
    printf(GRAY "Running clock unit tests...\n" RESET);

    test_parse_time();
    test_validate_time();
    test_print_time();
    test_next_second();
    test_next_minute();
    test_next_hour();

    printf("\nAll tests executed.\n");
    return 0;
}