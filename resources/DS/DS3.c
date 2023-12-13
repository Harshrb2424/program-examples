//! EXP3 IMPLEMENTATION OF CIRCULAR LINKED LIST
#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *next;
};
struct node *head = NULL, *p, *q, *t, *last = NULL;
void display(void);
void insert_begin(void);
void insert_after(void);
void insert_end(void);
void del_begin(void);
void del(void);
void del_end(void);
int x;
int main()
{
    int ch, n, i;
    // clrscr();
    printf("Enter the number of nodes:\t");
    scanf("%d", &n);
    t = head;

    for (i = 0; i < n; i++)
    {
        p = malloc(sizeof(struct node));
        printf("Enter the data of node%d \t", i + 1);
        scanf("%d", &p->data);
        p->next = NULL;
        if (head == NULL)
        {
            head = p;
            head->next = head;
        }
        else
        {
            t->next = p;
            p->next = head;
        }
        t = p;
    }
    last = t;
    display();
    printf("\nMenu:");
    printf("\n 1.Insert at beginning \n 2.Insert after the given node \n 3.Insert at end \n");
    printf(" 4.Delete at beginning \n 5.Delete the given node \n 6.Delete at last \n 7.Exit\n");
    do
    {
        printf("\nEnter the option \t");
        scanf("%d", &ch);
        t = head;
        switch (ch)
        {
        case 1:
            insert_begin();
            display();
            break;
        case 2:
            insert_after();
            display();
            break;
        case 3:
            insert_end();
            display();
            break;
        case 4:
            del_begin();
            display();
            break;
        case 5:
            del();
            display();
            break;
        case 6:
            del_end();
            display();
            break;
        case 7:
            printf("Thank You");
            // getch();
        }
    } while (ch != 7);
    return 0;
}
void insert_begin()
{
    p = malloc(sizeof(struct node));
    printf("Enter the data to be inserted\t");
    scanf("%d", &p->data);
    p->next = head;
    last->next = p;
    head = p;
}
void insert_after()
{
    printf("Enter the previous node value where the new node to be inserted \t");
    scanf("%d", &x);
    p = malloc(sizeof(struct node));
    printf("Enter the data to be inserted\t");
    scanf("%d", &p->data);
    t = head;
    while (x != t->data)
        t = t->next;
    if (t->next != head)
    {
        q = t->next;
        p->next = q;
        t->next = p;
    }
    else
    {
        t->next = p;
        last = p;
        p->next = head;
    }
}
void insert_end()
{
    p = malloc(sizeof(struct node));
    printf("Enter the data to be inserted\t");
    scanf("%d", &p->data);
    p->next = head;
    t = head;
    while (t->next != head)
        t = t->next;
    t->next = p;
    last = p;
}
void del_begin()
{
    t = head;
    head = head->next;
    t->next = NULL;
    free(t);
    last->next = head;
}
void del()
{
    printf("Enter the node value to be deleted \t");
    scanf("%d", &x);
    t = head;
    while (x != t->data)
    {
        p = t;
        t = t->next;
    }
    q = t->next;
    if (t == head)
    {
        head = head->next;
        last->next = head;
    }
    else if (t->next == head)
    {
        p->next = head;
        last = p;
    }
    else
        p->next = q;
    free(t);
}
void del_end()
{
    t = head;
    while (t->next != head)
    {
        p = t;
        t = t->next;
    }
    if (t == head)
        head = NULL;
    else
    {
        p->next = head;
        last = p;
        free(t);
    }
}
void display()
{
    printf("The circular linked list is \n");
    t = head;
    printf("-->");
    while (t != last)
    {
        printf("%d-->", t->data);
        t = t->next;
    }
    printf("%d-->", t->data);
}
