#include<stdio.h>
#include<iostream>
#include<vector>
#include<string>
#include<stdlib.h>
using namespace std;

int main()
{
	double a, b;
	while (cin >> a >> b) {
		try {
			double result = a / b;

			if (b != 0) {
				cout << "The result is: " << result << endl;
			}
			else {
				throw runtime_error("b should not be 0.");

			}
		}
		catch (runtime_error err) {
			cout << err.what()
				<< "Do you what to try again?(y/n)" << endl;
			char c;
			cin >> c;
			if (c == 'n' | !cin) {
				break;

			}
		}
	}
	
}