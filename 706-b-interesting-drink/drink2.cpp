#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> prices;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        prices.push_back(x);
    }

    sort(prices.begin(), prices.end());

    int q;
    cin >> q;

    for (int i = 0; i < q; i++)
    {
        int b;
        cin >> b;

        /* search for first iterator of element which is greater than b */
        auto upper = upper_bound(prices.begin(), prices.end(), b);
        cout << distance(prices.begin(), upper) << endl;
    }
}
