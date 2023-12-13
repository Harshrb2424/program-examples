#include <stdio.h>
#define n 5 // No.of processes
#define m 3 // No.of resouces
int main()
{
    // P0, P1, P2, P3, P4 are the Process names here
    int i, j, k, y=0, need[n][m], flag=1, f[n], ans[n], ind=0;
    int alloc[5][3] = { { 0, 1, 0 }, // P0 // Allocation Matrix
                        { 2, 0, 0 }, // P1
                        { 3, 0, 2 }, // P2
                        { 2, 1, 1 }, // P3
                        { 0, 0, 2 } // P4
    };
    int max[5][3] = { { 7, 5, 3 }, // P0 // MAX Matrix
                    { 3, 2, 2 }, // P1
                    { 9, 0, 2 }, // P2
                    { 2, 2, 2 }, // P3
                    { 4, 3, 3 } // P4
    };
    int avail[3] = { 3, 3, 2 }; // Available Resources
    
    for (k = 0; k < n; k++)
        f[k] = 0;
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            need[i][j] = max[i][j] - alloc[i][j];
    for (k = 0; k < 5; k++)
        {
        for (i = 0; i < n; i++)
            {
            if (f[i] == 0)
                {
                int flag = 0;
                for (j = 0; j < m; j++)
                    {
                    if (need[i][j] > avail[j])
                        {
                        flag = 1;
                        break;
                        }
                    }
                    if (flag == 0)
                    {
                        ans[ind++] = i;
                        for (y = 0; y < m; y++)
                            avail[y] += alloc[i][y];
                        f[i] = 1;
                    }
                }   
            }
        }
    for(i=0;i<n;i++)
        {
        if(f[i]==0)
            {
            flag=0;
            printf("The system is UNSAFE state");
            break;
            }
        }
    if(flag==1)
    {
        printf("The system is SAFE and safe sequence is \t");
        for (i = 0; i < n - 1; i++)
            printf(" P%d ->", ans[i]);
        printf(" P%d", ans[n - 1]);
    }
    return (0);
 }
