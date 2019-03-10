#include<iostream>
#include<stdexcept>
#include<stdlib.h>
using namespace std;
int main()
{
	cout << "请依次输入被除数和除数：" << endl;
	int ival1, ival2;
	while (cin >> ival1 >> ival2) {
		try {
			if (ival2 == 0) {
				throw runtime_error("除数不得为0");
			}
			cout << "两数相除的结果为：" << ival1/ival2 <<endl;
		}
		catch (runtime_error err) {
			cout << err.what() << endl;
			cout << "是否还要继续？（y/n）" << endl;
			char ch;
			cin >> ch;
			if (ch != 'y' && ch != 'Y') 
				break;
		}
	}
	return 0;

}