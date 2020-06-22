#include<stdio.h>
#include<string.h>
int main()
{
	char c[50], cp[50];
	gets(c);
	strcpy(cp, c);
	puts(c);
	puts(cp);
	return 0;
}
