#include<sys/stat.h> 
#include<stdio.h> 
#include<fcntl.h> 
#include<sys/types.h> 
int main() 
{ 
    int n,i=0; 
    int f1,f2; 
    char c,strin[100]; 
    f1=open("data.txt",O_RDWR|O_CREAT|O_TRUNC); 
    printf("Enter Data in data.txt: \n");
    while((c=getchar())!='\n') 
        strin[i++]=c; 
    strin[i]='\0'; 
    write(f1,strin,i); 
    close(f1); 
    f2=open("data.txt",O_RDONLY); 
    read(f2,strin,0); 
    printf("Data in data.txt:");
    printf("\n%s\n",strin); 
    close(f2); 
    return 0; 
} 