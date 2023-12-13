//! EXP6A IMPLEMENTATION OF BUBBLE SORT
#include <stdio.h>
#include <conio.h>
#define MAX 10
void printArray(int a[], int n)
{
    printf("[");
    for (int i = 0; i < n; i++)
        printf(" %d ", a[i]);
    printf("]\n");
}
void main()
{
    int a[MAX], n, i, j, temp;
    // clrscr();
    printf("Enter the total number of elements in an array : \t ");
    scanf("%d", &n);
    printf("Enter %d elements one by one \n", n);
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    printf("\n Input Array : ");
    printArray(a, n);
    for (i = 0; i < n - 1; i++)
    {
        printf("\n Iteration %d: \n\n", (i + 1));
        for (j = 0; j < n - 1 - i; j++)
        {
            printf("\t\t Items compared: [%d, %d] ", a[j], a[j + 1]);
            if (a[j] > a[j + 1])
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                printf(" => swapped [%d, %d]\n", a[j], a[j + 1]);
            }
            else
                printf(" => not swapped\n");
        }
        printf("\n\t Array after this iteration: ");
        printArray(a, n);
    }
    printf("\nOutput Array: ");
    printArray(a, n);
    // getch();
}