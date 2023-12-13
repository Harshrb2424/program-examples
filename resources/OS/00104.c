#include <stdio.h>
void main()
{
    int bt[10], p[10], wt[10], tat[10], pri[10], i, j, k, n, total = 0, pos, temp;
    float awt, atat;
    printf("Enter number of process: ");
    scanf("%d", &n);
    printf("\nEnter Burst Time:\n");
    for (i = 0; i < n; i++)
    {
        printf("p%d : ", i + 1);
        scanf("%d", &bt[i]);
        p[i] = i + 1; // contains process number
    }
    printf(" Enter priority of the process:\n");
    for (i = 0; i < n; i++)
    {
        p[i] = i + 1;
        printf("p%d : ", i + 1);
        scanf("%d", &pri[i]);
    }
    for (i = 0; i < n; i++)
        for (k = i + 1; k < n; k++)
            if (pri[i] > pri[k])
            {
                temp = p[i];
                p[i] = p[k];
                p[k] = temp;
                temp = bt[i];
                bt[i] = bt[k];
                bt[k] = temp;
                temp = pri[i];
                pri[i] = pri[k];
                pri[k] = temp;
            }
    wt[0] = 0; // waiting time for first process will be zero
    for (i = 1; i < n; i++)
    {
        wt[i] = 0;
        for (j = 0; j < i; j++)
            wt[i] += bt[j];
        total += wt[i];
    }
    awt = (float)total / n; // average waiting time
    total = 0;
    printf("\nProcess\t Burst Time \tPriority \tWaiting Time\tTurnaround Time");
    for (i = 0; i < n; i++)
    {
        tat[i] = bt[i] + wt[i]; // calculate turnaround time
        total += tat[i];
        printf("\n p%d \t\t %d \t\t %d \t\t %d \t\t %d", p[i], bt[i], pri[i], wt[i], tat[i]);
    }
    atat = (float)total / n; // average turnaround time
    printf("\n\n Average Waiting Time =%.2f", awt);
    printf("\n Average Turnaround Time=%.2f\n", atat);
}