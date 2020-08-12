#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int find_match(int budget, vector<int>::iterator begin, vector<int>::iterator end);

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
        cout << find_match(b, prices.begin(), prices.end()) << endl;
    }
}

int find_match(int budget, vector<int>::iterator begin, vector<int>::iterator end)
{
    auto start = begin;

    while (distance(begin, end))
    {
        auto middle = begin + distance(begin, end) / 2;

        if (*middle > budget)
        {
            end = middle;
        }
        else
        {
            begin = middle + 1;
        }
    }
    return distance(start, begin);
}
