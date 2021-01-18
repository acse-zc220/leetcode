#include <iostream>

using namespace std;

int addarray(int *array, int n);
int main(int argc, char *argv[]) {
	int data[] = {0,1,2,3,4,5};
	int size =sizeof(data) / sizeof(data[0]);
	cout << addarray(data,size)<<endl;
	return 0;
}

int addarray (int *array, int n)
{
	int sum = 0;
	int i;
	for ( i =0; i<n; i++)
	{
		sum += *array++;
	}
	return sum;
}