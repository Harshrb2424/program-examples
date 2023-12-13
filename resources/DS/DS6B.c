//! EXP6B IMPLEMENTATION OF SELECTION SORT
#include <stdio.h>
#include <conio.h>
void printArray(int arr[], int size)
{
    printf("[ ");
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("]\n");
}
int main()
{
    int a[20], i, j, n, min, t;
    // clrscr();
    printf("Enter the total elements in the array \t");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("Enter the element%d \t: ", i + 1);
        scanf("%d", &a[i]);
    }
    printf("\n Input Array : ");
    printArray(a, n);
    for (i = 0; i < n - 1; i++)
    {
        printf("\n Iteration %d: \n", (i + 1));
        min = i;
        for (j = i + 1; j < n; j++)
            if (a[j] < a[min])
                min = j;
        if (i != min)
        {
            t = a[min];
            a[min] = a[i];
            a[i] = t;
            printf("\t Items compared: [%d, %d] & swapped ", a[min], a[i]);
        }
        else
            printf("\t Not swapped ");
    }
    printf("\n\n Output Array: ");
    printArray(a, n);
    // getch();
    return 0;
}
