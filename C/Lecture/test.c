#include <stdio.h>

int main() {
  int n = 1, a = 2, b = 3, z;

  if (n > 0) {
    if (a > b) {
      z = a;
    } else {
      z = b;
    }
  }
  printf("%d\n", z);
  return 0;
}