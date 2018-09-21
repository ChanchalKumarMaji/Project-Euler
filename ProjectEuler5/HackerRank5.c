#include<stdio.h>
#include<math.h>
int main()
    {
    int T,i,j,sum=1,m,k;
int p[]={2,3,5,7,11,13,17,19,23,29,31,37};
scanf("%d",&T);
int n[T];    
for(i=0;i<T;i++)
    scanf("%d",n+i);
for(i=0;i<T;i++)
    {
    m=n[i];
    j=0;
    sum=1;
    while(p[j]<=m){
        k=floor(log(m)/log(p[j]));
        sum=sum*pow(p[j],(int)k);
        j=j+1;  }
        
    printf("%d\n",(int)sum);       
 
    }
    }
