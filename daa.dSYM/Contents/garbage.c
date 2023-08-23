#include <stdio.h> #include <stdlib.h>
#define N 11 #define W 25
typedef struct { int value;
int weight;
float ratio; } Item;
int cmpfunc(const void* a, const void* b) { Item* item1 = (Item*)a;
Item* item2 = (Item*)b;
return item2->ratio > item1->ratio;
}
float knapsack(Item items[]) { int i;
float total_value = 0;
int remaining_capacity = W;
qsort(items, N, sizeof(Item), cmpfunc);
for (i = 0; i < N; i++) {
if (items[i].weight <= remaining_capacity) {
total_value += items[i].value;
remaining_capacity -= items[i].weight; } else {
total_value += items[i].ratio * remaining_capacity;
break; }
}
return total_value; }
int main() {
Item items[N]; int i, r = 48;
for (i = 0; i < N; i++) {
items[i].value = r + (r+1)*i;
items[i].weight = (r+i)%10 + 1;
items[i].ratio = (float)items[i].value / items[i].weight;
}
// display values, weights, and ratios printf("Values:\n");
for (i = 0; i < N; i++) {
printf("%d ", items[i].value); }
printf("\n");
printf("Weights:\n"); for (i = 0; i < N; i++) {
printf("%d ", items[i].weight); }
printf("\n");
printf("Ratios:\n");
for (i = 0; i < N; i++) {
printf("%.2f ", items[i].ratio); }
printf("\n");
// display total profit
printf("Total profit: %.2f\n", knapsack(items));
return 0; }