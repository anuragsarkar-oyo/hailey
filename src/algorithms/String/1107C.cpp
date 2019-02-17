//
// Created by Anurag Sarkar on 2019-02-12.
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

/// Typedef
typedef long long int ll;

#define sc1(a) scanf("%lld",&a)
#define sc2(a,b) scanf("%lld %lld",&a,&b)

#define pf1(a) printf("%lld\n",a)
#define pf2(a,b) printf("%d %d\n",a,b)

#define mx 10000007
#define mod 1000000007
#define PI acos(-1.0)

#define size1 1000

int dr[] = {-2,-2,-1,-1,1,1,2,2};
int dc[] = {-1,1,-2,2,-2,2,-1,1};

int main()
{
    ll num, k;

    sc2(num, k);

    ll arr[num];

    for(ll i = 0; i < num; i++)
        sc1(arr[i]);

    string str;
    cin >> str;

    ll ans = 0;
    for(ll i = 0; i < num; i++){
        ll j = i;

        vector <ll> sum;

        while (j < num && str[i] == str[j]){
            sum.push_back(arr[j]);
            j++;
        }

        sort(sum.rbegin(), sum.rend());

        ll siz = sum.size();
        // cout << siz << " siz : k " << k << endl;

        for(ll tc = 0; tc < min(k, siz); tc++){
            ans += sum[tc];
            //cout << sum[tc] << " ";
        }

        i = j - 1;
    }

    pf1(ans);
}