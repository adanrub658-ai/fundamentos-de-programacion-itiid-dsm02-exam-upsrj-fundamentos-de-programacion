#ifndef CLOCK_H
#define CLOCK_H

int parse_time(const char *time_str, int *h, int *m, int *s);
int validate_time(int h, int m, int s);
void print_time(int h, int m, int s);
int next_second(int s);
int next_minute(int m, int s);
int next_hour(int h, int m, int s);

#endif