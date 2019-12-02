#include <stdio.h>

int main(void) {

  for ( int i=1; i <= 100; i++ ) {
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
