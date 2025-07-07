#include <iostream>
#include <array>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n, j, k;
        cin >> n >> j >> k;
        string answer = "no";

        vector<int> a(n);
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        int max_a = *max_element(a.begin(), a.end());
        if (k > 1 || a[j - 1] >= max_a)
        {
            answer = "yes";
        }

        cout << answer << endl;
    }
}
