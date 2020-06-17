#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <sys/types.h>

#define ARR_SIZE 1024 * 1024 * 1024
int *arr;

void* f_thread(void *v) {
  arr = (int*)malloc(ARR_SIZE * sizeof(int) + 1);
  time_t t;
  int i;

  /* Intializes random number generator */
  srand((unsigned) time(&t));

  while (1) {
    i = arr[rand() % ARR_SIZE];
    ++i;
    arr[rand() % ARR_SIZE] = 1;
  }
}

int main(int argc, char **argv) {
  if (argc != 2) {
     printf("One argument expected: Execution time in seconds\n");
     return 0;
  }

  sleep(atoi(argv[1]));

  pthread_t thr;
  pthread_create(&thr, NULL, f_thread, NULL);

  sleep(atoi(argv[1]));

  pthread_cancel(thr);
  free(arr);

  return 0;
}
