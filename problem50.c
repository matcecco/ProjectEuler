#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdint.h>
#include <windows.h>

#include "euler_util.h"


int check(struct elem* p);

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
			push_back(&tail,i);
			check(primi);
		}
	}
	printf("time elapsed %f",get_timer());
	return 0;
}

int check(struct elem* p)
{
	static int max=-1;

	struct elem* f;
	uint64_t sum=0;
	int count=0;

	for(f=p;f;f=f->next)
	{
		sum+=f->n;
		count++;
	}
	for(f=p;f;f=f->next)
	{
		if(max>count)
			return 0;
		if(sum < 1000000 && is_prime(sum))
		{
			if(max<count)
			{
				printf("found %llu with %d consec primes\n",sum,count);
				max=count;
			}
			return count;
		}
		sum-=f->n;
		count--;
	}
	
	return 0;
}
