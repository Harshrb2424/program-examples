#include <stdio.h>
void main()
{
    int bt[10], p[10], wt[10], tat[10], i, j, n, total = 0, pos, temp;
    float awt, atat;
    printf(" Enter the number of process: ");
    scanf("%d", &n);
    printf("\nEnter Burst Time:\n");
    for (i = 0; i < n; i++)
    {
        printf("p%d:", i + 1);
        scanf("%d", &bt[i]);
        p[i] = i + 1; // contains process number
    }
    // sorting burst time in ascending order using selection sort
    for (i = 0; i < n; i++)
    {
        pos = i;
        for (j = i + 1; j < n; j++)
        {
            if (bt[j] < bt[pos])
                pos = j;
        }
        temp = bt[i];
        bt[i] = bt[pos];
        bt[pos] = temp;
        temp = p[i];
        p[i] = p[pos];
        p[pos] = temp;
    }
    wt[0] = 0; // waiting time for first process will be zero
    // calculate waiting time
    for (i = 1; i < n; i++)
    {
        wt[i] = 0;
        for (j = 0; j < i; j++)
            wt[i] += bt[j];
        total += wt[i];
    }
    awt = (float)total / n; // average waiting time
    total = 0;
    printf("\n Process \t Burst Time \t Waiting Time \t Turn Around Time");
    for (i = 0; i < n; i++)
    {
        tat[i] = bt[i] + wt[i]; // calculate turnaround time
        total += tat[i];
        printf("\n p%d \t\t %d \t\t %d \t\t %d", p[i], bt[i], wt[i], tat[i]);
    }
    atat = (float)total / n; // average turnaround time
    printf("\n\n Average Waiting Time =%.2f", awt);
    printf("\n Average Turnaround Time=%.2f\n", atat);
}
