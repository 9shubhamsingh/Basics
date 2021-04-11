#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
 

int main()
{	
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

	ll n;
	cin >> n;
	if (n==1)
	{
		cout << n;
		return 0;
	}	
	if(n==2||n==3)
	{
		cout << "NO SOLUTION";
		return 0;
	}
	//4 2 3 1
	if(n%2==0)
	{
		for(int i=2; i<=n; i+=2)
		{
			cout << i << " ";
		}
		for(int i=1; i<n; i+=2)
		{
			cout << i << " ";
		} 
	}
	else
	{
		for(int i=n-1; i>0; i-=2)
		{
			cout<< i << " ";
		}
		for(int i=n; i>0; i-=2)
		{
			cout<< i << " "; 
		}
	}
	
	/* code */
	return 0;

}