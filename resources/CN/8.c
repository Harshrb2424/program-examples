#include<stdio.h> 
#include<conio.h>
#define MAX 25 
#define min(x,y) ((x)<(y)? (x):(y)) 
int main() 
{ 
 int cap, oprt,nsec,cont,i=0,inp[MAX],ch; 
 clrscr(); 
 printf("Enter the bucket size:\n"); 
 scanf("%d",&cap); 
 printf("Enter the accepted rate:\n"); 
 scanf("%d",&oprt); 
 do 
 { 
 printf("Enter the number of packets entering at %d seconds: ",i+1); 
 scanf("%d",&inp[i]); 
 i++; 
 printf("Enter 1 to insert packets or 0 to quit\n"); 
 scanf("%d",&ch); 
 }while(ch); 
 
 nsec=i; 
 printf("\n seconds \t packets received \t packets sent \t packets left in bucket\n"); 
 cont=0; 
 
 for(i = 0; i < nsec; i++) 
 { 
 cont += inp[i]; 
 if(cont > cap) 
 cont = cap; 
 printf(" %d ",(i+1)); 
 printf("\t\t %d ",inp[i]); 
 printf("\t\t\t\t %d ",min(cont,oprt)); 
 cont=cont - min(cont,oprt); 
 printf("\t\t %d \n",cont); 
 } 
for( i=0; cont != 0; i++) 
 { 
 if(cont > cap) 
 cont = cap; 
 printf(" %d ",(i+1)); 
 printf("\t\t 0 "); 
 printf("\t\t\t\t %d ",min(cont,oprt)); 
 cont=cont - min(cont,oprt); 
 printf("\t\t %d \n",cont); 
 } 
 getch();
 return(0); 
}
