#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct frame {
    int sno;
    char msg[15];
    int flag;
};

int main() {
    int i, j, n, r, k;
    clrscr();
    printf("Enter the number of frames: ");
    scanf("%d", &n);

    struct frame fr[n];
    int s[n];
    for (i = 0; i < n; i++) {
        s[i] = -1;
        fr[i].sno = -1;
    }

    printf("Enter the messages:\n");
    for (i = 0; i < n; i++) {
        scanf("%s", fr[i].msg);
        fr[i].sno = i;
    }

    srand(time(NULL)); // Seed for randomness
    for (j = 0; j < n; j++) {
        r = rand() % n;
        if (s[r] == -1) {
            fr[j].flag = r;
            s[r] = 1;
        } else {
            for (k = 0; k < n; k++) {
                if (s[k] == -1) {
                    fr[j].flag = k;
                    s[k] = 1;
                    break;
                }
            }
        }
    }

    printf("\nArrived frames are:\n");
    printf(" sno\tmsg\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (fr[j].flag == i) {
                printf(" %d\t%s\n", fr[j].sno, fr[j].msg);
            }
        }
    }

    // Sort frames by sno
    for (i = 0; i < n; i++) {
        for (j = 0; j < n - 1; j++) {
            if (fr[j].sno > fr[j + 1].sno) {
                struct frame temp = fr[j];
                fr[j] = fr[j + 1];
                fr[j + 1] = temp;
            }
        }
    }

    printf("\nAfter sorting arrived frames are:\n");
    printf(" sno\tmsg\n");
    for (i = 0; i < n; i++) {
        printf(" %d\t%s\n", fr[i].sno, fr[i].msg);
    }
    getch();
    return 0;
}
