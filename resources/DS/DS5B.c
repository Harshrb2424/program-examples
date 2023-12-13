//! EXP5B IMPLEMENTATION OF QUEUE USING LINKED LIST
#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
} *front = NULL, *rear = NULL;
void insert(int);
void delete();
void display();
void main()
{
    int choice, value;
    // clrscr();
    printf("\n:: Queue Implementation using Linked List ::\n");
    printf("\n****** MENU ******\n");
    printf(" 1. Insert\n 2. Delete\n 3. Display\n 4. Exit\n");
    while (1)
    {
        printf("\n Enter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter the value to be insert: ");
            scanf("%d", &value);
            insert(value);
            break;
        case 2:
            delete ();
            break;
        case 3:
            display();
            break;
        case 4:
            printf("\nThank you\n");
            // getch();
            exit(0);
        default:
            printf("\n Wrong selection!!! Please Enter Correct Choice!!!\n");
        }
    }
}
void insert(int value)
{
    struct Node *p;
    p = malloc(sizeof(struct Node));
    p->data = value;
    p->next = NULL;
    if (front == NULL)
        front = rear = p;
    else
    {
        rear->next = p;
        rear = p;
    }
    printf("\n Insertion is Success!!!\n");
}
void delete()
{
    if (front == NULL)
        printf("\n Queue is Underflow!!!\n");
    else
    {
        struct Node *temp = front;
        front = front->next;
        printf("\n Deleted element: %d\n", temp->data);
        free(temp);
    }
}
void display()
{
    if (front == NULL)
        printf("\n Queue is Empty!!!\n");
    else
    {
        struct Node *temp = front;
        while (temp->next != NULL)
        {
            printf("%d--->", temp->data);
            temp = temp->next;
        }
        printf("%d--->NULL\n", temp->data);
    }
}