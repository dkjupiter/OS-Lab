#include <stdio.h>
int main() {
  int a = 1;
  int sum = 0;
  float count = 0;
  while(a>0){
        printf("enter a number : ");
        scanf("%d",&a);
        if(a>0){
           sum += a;
           count++;
        }
  }
  float avr = (float)sum/count;
  printf("sum = %d ", sum);
  printf("average = %0.2f " , avr);
}
