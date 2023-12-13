//! EXP7B IMPLEMENTATION OF BINARY SEARCH
#include <stdio.h>
void printResult(int);
int BinarySearch(int array[], int start, int last, int element)
{
    while (start <= last)
    {
        int middle = (last + start) / 2;
        if (array[middle] == element)
            return middle;
        if (array[middle] < element)
            start = middle + 1;
        else
            last = middle - 1;
    }
    return -1;
}
int RecursiveBSearch(int array[], int start, int last, int element)
{
    while (start <= last)
    {
        int middle = (last + start) / 2;
        if (array[middle] == element)
            return middle;
        if (array[middle] > element)
            return RecursiveBSearch(array, start, middle - 1, element);
        return RecursiveBSearch(array, middle + 1, last, element);
    }
    return -1;
}
int main(void)
{
    int a[30], n, element, temp, option;
    printf("Enter the total number of elements in the array : ");
    scanf("%d", &n);
    printf("Enter the elements one by one \n");
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    printf("Enter the element to be searched : ");
    scanf("%d", &element);
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - 1 - i; j++)
        {
            if (a[j] > a[j + 1])
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
    printf("The sorted Array is \n");
    for (int i = 0; i < n; i++)
        printf(" %d ", a[i]);
    int ans = BinarySearch(a, 0, n - 1, element);
    printf("\n\n Result : Binary Search using Non-recursive function \n");
    printResult(ans);
    int result = RecursiveBSearch(a, 0, n - 1, element);
    printf("\n Result : Binary Search using Recursive function \n");
    printResult(result);
    return 0;
}
void printResult(int X)
{
    if (X == -1)
        printf("\t Element not found in this array ");
    else
        printf("\t Element found at position %d \n", X + 1);
}
