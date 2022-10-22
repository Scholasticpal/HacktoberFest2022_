// Given a sequence a1,a2,…,an, find the minimum number of elements to remove from the sequence such that after the removal, the sum of every 2 consecutive elements is even.
#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while (t--){
        int n;
        cin>>n;
        int od = 0, ev = 0;

        for (int i = 0 ; i<n ; i++){
            int x;
            cin>>x;
            if (x & 1){
                od++;
            }
            else {ev++;}
        }
        cout<<min(od,ev)<<endl;
        }

}