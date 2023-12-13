#include <stdio.h>
void main()
{
    int bt[10], p[10], wt[10], tat[10], i, j, n, total = 0;
    float awt, atat;
    printf("Enter the total number of processes: ");
    scanf("%d", &n);
    printf("\n Enter Burst Time:\n");
    for (i = 0; i < n; i++)
    {
        printf("p%d : ", i + 1);
        scanf("%d", &bt[i]);
    }
    wt[0] = 0; // waiting time for first process will be zero
    // calculate waiting time for remaining process
    for (i = 1; i < n; i++)
    {
        wt[i] = 0;
        for (j = 0; j < i; j++)
            wt[i] += bt[j];
        total += wt[i];
    }
    awt = (float)total / n; // average waiting time
    total = 0;
    printf("\n Process\t Burst Time \t Waiting Time\t Turnaround Time");
    for (i = 0; i < n; i++)
    {
        tat[i] = bt[i] + wt[i]; // calculate turnaround time
        total += tat[i];
        printf("\n p%d \t\t %d \t\t %d\t\t %d", i + 1, bt[i], wt[i], tat[i]);
    }
    atat = (float)total / n; // average turnaround time
    printf("\n\n Average Waiting Time = %.2f", awt);
    printf("\n Average Turnaround Time = %.2f\n", atat);
}
