#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;

    int a;
    vector<int> vec;
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        vec.push_back(a);
    }

    sort(vec.rbegin(), vec.rend());

    if (k > vec.size())
    {
        cout << -1 << endl;
        return 0;
    }
    cout << vec[k - 1] << " " << 1 << endl;
}