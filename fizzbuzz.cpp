#include <iostream>

using namespace std;

int main(void) {
  const int MAX_NUM = 100;

  ios_base::sync_with_stdio(false); // using std::endl forces flush

  for ( int i=1; i <= MAX_NUM; i++ ) {
    int fizz = i % 3, buzz = i % 5;

    if ( !fizz || !buzz ) {
      cout << (!fizz ? "fizz" : "") << (!buzz ? "buzz" : "") << "\n";
    } else {
      cout << i << "\n";
    }

  }

  return 0;

}
