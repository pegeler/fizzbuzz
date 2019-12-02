#include <iostream>

using namespace std;

int main(void) {
  for ( int i=1; i <= 100; i++ ) {
    int fizz = i % 3, buzz = i % 5;

    if ( !fizz || !buzz ) {
      cout << (!fizz ? "fizz" : "") << (!buzz ? "buzz" : "") << endl;
    } else {
      cout << i << endl;
    }

  }

  return 0;

}
