#include<stdio.h>
#include<iostream>
#include<vector>
#include<string>
#include<stdlib.h>
using namespace std;

int fact(int val)
{
	int i = 1;
	while (val != 1) {
		i *= --val;

	}return i;

}
int main()
{
	int i;
	cout << "计算阶乘，请输入数字：" << endl;
	cin >> i;
	cout << "结果为：" << fact(i) << endl;
	
}