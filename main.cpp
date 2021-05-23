#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
 

int main()
{	
	 #ifndef ONLINE_JUDGE
	 freopen("input.txt", "r", stdin);
	 freopen("output.txt", "w", stdout);
	 #endif

	 int n;
	 cin >> n;

	 int a[n];
	 for(int i =0; i < n; i++)
	 {
	 	cin >> a[i];
	 }


	 for(int i = 0; i<n;i++)
	 {
	 	if(a[i]!=0)
		{
			if(a[i+1]!=0)
			{
				a[i] = a[i]*2;
				cout << a[i] << "\n";
				a[i+1] = 0;
			}
		}
		else
		{
			for (int j = i; j < n; j++)
				{
			      int p = 0;
			      p = a[j+1];
			      a[j+1] = a[j];
			      a[j] = p;			
				}
		}
	 }
	
	for(int i=0;i<n;i++)
	{
		cout << a[i] <<" ";
	}
	
	/* code */
	return 0;

}