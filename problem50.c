#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdint.h>
#include <windows.h>

#include "euler_util.h"



int main()
{
	struct elem* primi;
	struct elem* tail;
	int i;

	start_timer();

	primi=tail=malloc(sizeof(struct elem));
	primi->n=2;
	primi->next=0;

	for(i=3;i<5000;i+=2)
	{
		if(is_prime(i))
		{
			push(&tail,i);
			check(primi);
		}
	}
	printf("time elapsed %f",get_timer());
	return 0;
}
