#include<stdio.h>
#include<iostream>
#include<vector>
#include<string>
#include<stdlib.h>
using namespace std;

size_t count_calls()
{
	static size_t ctr = 0;
	return ++ctr;
}
int main()
{
	for (int i = 0; i != 10; ++i) {
		cout << count_calls() << endl;

	}
	system("pause");
	
}