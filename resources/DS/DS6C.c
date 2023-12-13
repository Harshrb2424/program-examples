//! EXP6C IMPLEMENTATION OF INSERTION SORT
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
    int a[20], i, j, n, NewElement, flag;
    // clrscr();
    printf("Enter the total number of elements in an array : \t");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("Enter the element%d \t: ", i + 1);
        scanf("%d", &a[i]);
    }
    printf("\n\n Input Array : ");
    printArray(a, n);
    for (i = 1; i < n; i++)
    {
        NewElement = a[i];
        j = i - 1;
        flag = 0;
        while (j >= 0 && a[j] > NewElement)
        {
            a[j + 1] = a[j];
            j = j - 1;
            flag = 1;
        }
        a[j + 1] = NewElement;
        printf("\n Iteration %d : \n", i);
        if (flag == 1)
            printf("\t %d is taken & inserted \n", NewElement);
        else
            printf("\t %d is taken & kept at same position \n", NewElement);
        printf("\t\t Array after the iteration : ");
        printArray(a, n);
    }
    printf("\n Output Array: ");
    printArray(a, n);
    // getch();
    return 0;
}
