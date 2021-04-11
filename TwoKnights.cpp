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
	for(int k =1; k<=n; k++)
	{
		ll a1 = k*k, a2=a1*(a1-1)/2;
		if(k>2)
		{
			a2-=4*(k-1)*(k-2);
		}
		cout << a2 << "\n";
	}
	
	/* code */
	return 0;

}