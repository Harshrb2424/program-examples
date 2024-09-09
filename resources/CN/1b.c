#include <stdio.h>
#include <string.h> 
#include <conio.h>  // For older compilers, optional for modern compilers

int main() {
    char sdel[] = "DLESTX", data[50] = "", sdata[50] = ""; 
    int i = 0, j = 0;

    // Clear screen (optional, only for Turbo C/C++)
    clrscr();  // Remove this if using modern compilers like GCC

    // Input the message
    printf("Enter the message \t\t: "); 
    scanf("%s", data);

    // Convert all lowercase characters to uppercase
    for (int k = 0; data[k] != '\0'; k++) {
        if (data[k] >= 'a' && data[k] <= 'z') {
            data[k] = data[k] - 32;
        }
    }

    // Display the original message in uppercase
    printf("Original Message is \t: %s \n", data);

    // If the message is shorter than 3 characters, no special handling
    if (strlen(data) < 3) {
        strcat(sdel, data); 
        strcat(sdel, "DLEETX");
        printf("Message after character stuffing is \t: %s\n", sdel);
    } 
    else {
        // Perform character stuffing
        while (data[i] != '\0') {
            // Check if the current substring is "DLE"
            if (data[i] == 'D' && data[i+1] == 'L' && data[i+2] == 'E') {
                strcat(sdata, "DLEDLE");  // Add an extra "DLE" for escaping
                i += 3;  // Skip over "DLE"
                j += 6;  // Move to the next position in the stuffed data
                continue;
            }

            // Add the character to the stuffed data
            sdata[j] = data[i];
            j++;
            i++;
        }

        // Append "DLEETX" to mark the end of the message
        strcat(sdel, sdata); 
        strcat(sdel, "DLEETX");

        // Output the stuffed message
        printf("Message after stuffing is \t: %s\n", sdel);
    }

    // Pause output (optional, use only if needed)
    getch();  // Remove if using modern compilers like GCC

    return 0;
}
