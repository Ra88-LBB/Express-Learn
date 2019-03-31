#include<vector>
#include<string>
#include<fstream>
#include<iostream>
using namespace std;

int main()
{
	ifstream myfile("C:\\Users\\yl601\\Desktop\\Test\\1.txt");
	ofstream outfile
	("C:\\Users\\yl601\\Desktop\\Test\\1-change.txt", ios::app);
	string temp;
	if (!myfile.is_open())
	{
		cout << "未打开文件" << endl;
	}
	while (getline(myfile, temp))
	{
		outfile << temp;
		outfile << endl;
	}
	myfile.close();
	outfile.close();
	return 0;
}