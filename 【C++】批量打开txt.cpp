#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
	string str, tem;
	for (int i = 1; i < 9; ++i) {
		char Test[20];
		sprintf_s(Test, "%s%d%s",
			"Data\\Test", i, ".txt");
		ifstream file_name(Test);
		if (!file_name.is_open()) {
			cout << "Open file error!" << endl;
			return 0;
		}
		file_name >> tem;
		str = str + tem + '\n';
		file_name.close();
	}
	cout << str;

	system("pause");

	return 0;
}