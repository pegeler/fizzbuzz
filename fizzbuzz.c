#include <stdio.h>

#define MAX_NUM 100

int main(void) {

  for ( int i=1; i <= MAX_NUM; i++ ) {
    int fizz = i % 3, buzz = i % 5;

    if ( !fizz || !buzz ) {
      printf("%s%s\n",
          !fizz ? "fizz" : "",
          !buzz ? "buzz" : ""
      );
    } else {
      printf("%i\n", i);
    }

  }

  return 0;

}
