#include <stdio.h> 
#include <string.h> 
#include <conio.h>  // Use this only if working on Turbo C/C++ or similar IDE (Optional for modern compilers)

// Main function to implement bit stuffing
int main() {
    char ch, arr[50], fs[50] = "", t[50] = ""; 
    int count = 0, i = 0, j = 0;

    // Clear screen (Only relevant for Turbo C/C++)
    clrscr();  // Remove this line if using modern compilers like GCC

    // Input the bit string
    printf("Enter the bit string : \t"); 
    scanf("%s", arr);

    // Append flag "01111110" at the start of the final string
    strcat(fs, "01111110-"); 

    // If the string length is less than 5, no need for stuffing
    if (strlen(arr) < 5) {
        strcat(fs, arr); 
        strcat(fs, "-01111110");
        printf("The bits after stuffing are\n %s", fs);
    } 
    else {
        // Perform bit stuffing
        while ((ch = arr[j]) != '\0') {
            if (ch == '1') {
                ++count; 
            } 
            else {
                count = 0; 
            }

            // Add the bit to the temporary string
            t[i++] = ch; 

            // Insert a '0' after five consecutive '1's
            if (count == 5) {
                t[i++] = '0';
                count = 0;
            }

            // Move to the next bit
            j++;
        }
        t[i] = '\0'; // Terminate the temporary string

        // Append flag "01111110" at the end of the temporary string
        strcat(t, "-01111110"); 
        strcat(fs, t);

        // Output the stuffed string
        printf("The bits after bit stuffing are\n %s", fs);
    }

    // Pause the output (Use only if required in your environment)
    getch();  // Remove this line if using modern compilers like GCC

    return 0;
}
