#include <iostream>
#include <string>

using namespace std;

class ShubhClass
{
public:
	void setName(string z)
	{
		name = z;
	}
	string getName()
	{
		return name;
	}
private:
	string name;
};

int main()
{
	ShubhClass shu;
	shu.setName("Hero");
	cout << shu.getName();

	return 0;
}

