#include <stdio.h>
#include <stdlib.h>
#define MAX_ARRAY_SIZE 128
void max_array(int* array, char* str)
{
    int rqm = 0;

    while (str[rqm] != '\0')
    {
        if (str[rqm] != '"')
        {
            array[(int)str[rqm]] += 1;
        }
        rqm = rqm + 1;
    }
}

void count_array(int* array, int size_array)
{
    int rqm2 = 0;

    while (rqm2 < size_array)
    {
        if (array[rqm2] > 0)
        {
            printf("%c:%d\n", rqm2, array[rqm2]);
        }
        rqm2 = rqm2 + 1;
    }
}

int main(int a, char** b)
{
    int rqm3 = 1;
    int array[MAX_ARRAY_SIZE] = {0};

    while (rqm3 < a)
    {
        max_array(&array[0], b[rqm3]);
        rqm3 = rqm3 + 1;
    }
    count_array(&array[0], MAX_ARRAY_SIZE);
    return EXIT_SUCCESS;
}