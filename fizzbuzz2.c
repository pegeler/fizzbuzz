#include <stdio.h>

#define MAX_NUM 100

typedef struct {
  int three;
  int five;
} Modulus;

int main()
{
  Modulus m;
  m.three = m.five = 0;
  for (int i=1; i <= MAX_NUM; i++) {

    /* fizz */
    if (++m.three == 3) {
      m.three = 0;
      fputs("fizz", stdout);
    }

    /* buzz */
    if (++m.five == 5) {
      m.five = 0;
      fputs("buzz", stdout);
    }

    /* otherwise */
    if (m.three && m.five)
      printf("%d", i);

    putchar('\n');
  }

  return 0;
}
