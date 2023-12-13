//! EXP7A IMPLEMENTATION OF LINEAR SEARCH
#include <stdio.h>
void printResult(int);
int LinearSearch(int array[], int n, int x)
{
    for (int i = 0; i < n; i++)
        if (array[i] == x)
            return i;
    return -1;
}
int RecursiveLSearch(int arr[], int value, int index, int n)
{
    if (index >= n)
        return 0;
    else if (arr[index] == value)
        return index;
    else
        return RecursiveLSearch(arr, value, index + 1, n);
    return -1;
}
int main()
{
    int n, value, array[30];
    printf("Enter the total elements in the array ");
    scanf("%d", &n);
    printf("Enter the array elements \n");
    for (int i = 0; i < n; i++)
        scanf("%d", &array[i]);
    printf("Enter the element to search : ");
    scanf("%d", &value);
    int result = LinearSearch(array, n, value);
    printf("\n\n Result : Linear Search using Non-recursive function \n");
    printResult(result);
    int pos = RecursiveLSearch(array, value, 0, n);
    printf("\n\n Result : Linear Search using Recursive function \n");
    printResult(pos);
    return 0;
}
void printResult(int X)
{
    if (X != -1)
        printf("\t Element found at position %d ", X + 1);
    else
        printf("\t Element not found");
}
