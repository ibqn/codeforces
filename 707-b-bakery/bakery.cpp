#include <iostream>
#include <tuple>
#include <vector>
#include <unordered_set>
#include <climits>

using namespace std;

int main()
{
    int n, m, k;

    cin >> n >> m >> k;

    vector<tuple<int, int, int>> roads;
    for (int i = 0; i < m; i++)
    {
        int c1, c2, w;
        cin >> c1 >> c2 >> w;
        roads.push_back({c1, c2, w});
    }

    unordered_set<int> storages;
    for (int i = 0; i < k; i++)
    {
        int s;
        cin >> s;
        storages.insert(s);
    }

    unordered_set<int> costs;

    for (auto const &road : roads)
    {
        bool c1 = storages.find(get<0>(road)) != storages.end();
        bool c2 = storages.find(get<1>(road)) != storages.end();

        if (c1 != c2)
        {
            costs.insert(get<2>(road));
        }
    }

    if (costs.size())
    {
        int min_cost = INT_MAX;
        for (auto const &cost : costs)
        {
            min_cost = min(min_cost, cost);
        }

        cout << min_cost;
    }
    else
    {
        cout << -1;
    }

    cout << endl;
}
