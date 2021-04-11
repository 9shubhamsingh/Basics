#include<bits/stdc++.h>
using namespace std;

 #define ll long long

int main()
{	
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

	ll n;
	cin >> n;
	int mx = 0;
	ll ans = 0;
	for (int i = 0; i < n ; i++)
	{
		int x;
		cin >> x;
		mx = max(x,mx);
		ans+=mx-x;
	}
	cout << ans;
	
	/* code */
	return 0;

}