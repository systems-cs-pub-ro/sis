#include<stdlib.h>
#include<stdio.h>

int array[10];

int sum()
{
  unsigned i, sum;

  sum = 0;
  for(i = 0; i < 10; i++)
    sum += array[i];

  return sum;
}
