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
	
	cin >> n ;

	ll arr1[n];
	int i = 0;
	while (i <= n){
		arr1[i] = 0;
		i++;
	}

	for (int i = 0; i < n-1; i++)
	{
		int a, diff;
		cin >> a;
		diff = n-a;
		arr1[n - 1 - diff] = a;
	}
	for(i = 0; i <= n-1 ; i++)
	{
		if (arr1[i] == 0)
		{
			cout << i+1;
			break;
		}
	}
	
	/* code */
	return 0;

}