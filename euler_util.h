
double PCFreq = 0.0;
uint64_t CounterStart = 0;



struct elem
{
	int n;
	struct elem* next;
};

int is_prime(int n)
{
	if(n==2)
		return 1;
	if(n%2==0 || n<2)
		return 0;

	int i,sqr = sqrt(n);
	for(i=3;i<=sqr;i+=2)
		if(n%i==0)
			return 0;
	return 1;
}
void push(struct elem** t,int n)
{
	struct elem* e = malloc(sizeof(struct elem));
	e->n = n;
	e->next = 0;
	(*t)->next = e;
	*t = e;
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

void start_timer()
{
    LARGE_INTEGER li;
    if(!QueryPerformanceFrequency(&li))
		printf("Error start_timer()!\n");

    PCFreq = ((double)li.QuadPart);

    QueryPerformanceCounter(&li);
    CounterStart = li.QuadPart;
}
double get_timer()
{
    LARGE_INTEGER li;
    QueryPerformanceCounter(&li);
    return ((double)li.QuadPart-CounterStart)/PCFreq;
}
