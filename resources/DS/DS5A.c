//! EXP5A IMPLEMENTATION OF QUEUE USING ARRAY
#include <stdio.h>
#include <stdlib.h>
#define MAX 3
void insert();
void del();
void display();
int a[MAX], value, rear = -1, front = -1;
int main()
{
    int choice;
    // clrscr();
    printf("MENU \n");
    printf("1.Insert an element to queue \n");
    printf("2.Delete element from queue \n");
    printf("3.Display all elements of queue \n");
    printf("4.Quit \n");
    while (1)
    {
        printf("\nEnter your choice : ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            insert();
            break;
        case 2:
            del();
            break;
        case 3:
            display();
            break;
        case 4:
            printf("Thank You");
            // getch();
            exit(1);
        default:
            printf("Wrong choice \n");
        }
    }
}
void insert()
{
    if (rear == MAX - 1)
        printf("Queue Overflow \n");
    else
    {
        if (front == -1)
            front = 0;
        printf("Enter the value to be inserted into queue : ");
        scanf("%d", &value);
        rear = rear + 1;
        a[rear] = value;
    }
}
void del()
{
    if (front == -1 || front > rear)
    {
        printf("Queue Underflow \n");
        front = rear = -1;
        return;
    }
    else
    {
        printf("Element deleted from queue is : %d \n", a[front]);
        front = front + 1;
    }
}
void display()
{
    int i;
    if (front > rear || rear == -1)
        printf("Queue is empty \n");
    else
    {
        printf("Queue is : \n");
        for (i = front; i <= rear; i++)
            printf("%d \t", a[i]);
        printf("\n");
    }
}