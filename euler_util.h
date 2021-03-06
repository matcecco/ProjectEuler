//list
struct elem
{
	int n;
	struct elem* next;
};

void push_back(struct elem** t,int n) 
{
	struct elem* e = malloc(sizeof(struct elem));
	e->n = n;
	e->next = 0;
	(*t)->next = e;
	*t = e;
}

//timer

double PCFreq = 0.0;
uint64_t CounterStart = 0;

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

//prime numbers
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