//! EXP4B IMPLEMENTATION OF STACK USING LINKED LIST
#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
};
struct Node *top = NULL;

void push(int value)
{
    struct Node *p;
    p = malloc(sizeof(struct Node));
    p->data = value;
    if (top == NULL)
        p->next = NULL;
    else
        p->next = top;
    top = p;
}

void pop()
{
    if (top == NULL)
        printf("\n Stack is Underflow \n");
    else
    {
        struct Node *t = top;
        printf("The Popped element is %d \n ", t->data);
        top = top->next;
        free(t);
    }
}

void display()
{
    if (top == NULL)
        printf("\nStack Underflow\n");
    else
    {
        printf("The stack is \n");
        struct Node *t = top;
        while (t->next != NULL)
        {
            printf("%d--->", t->data);
            t = t->next;
        }
        printf("%d--->NULL\n", t->data);
    }
}

int main()
{
    int choice, value;
    // clrscr();
    printf("\n Implementation of Stack using Linked List ");
    printf("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n");
    printf(" 1. Push \n 2. Pop \n 3. Display \n 4. Exit \n");
    while (1)
    {
        printf("Enter your choice : ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("\nEnter the value to insert: ");
            scanf("%d", &value);
            push(value);
            break;
        case 2:
            pop();
            break;
        case 3:
            display();
            break;
        case 4:
            printf("\n Thank You \n");
            // getch();
            exit(0);
            break;
        default:
            printf("\n Wrong Choice \n");
        }
    }
}