#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>

using namespace std;

int main()
{
    int n, max_cap;
    cin >> n >> max_cap;

    pair<int, int> one[n];
    pair<int, int> two[n];

    int type, cap;
    int size_one, size_two;

    size_one = size_two = 0;
    for (int i = 1; i <= n; i++)
    {
        cin >> type >> cap;

        switch (type)
        {
        case 1:
            one[size_one++] = make_pair(cap, i);
            break;
        case 2:
            two[size_two++] = make_pair(cap, i);
            break;
        }
    }

    function<bool(pair<int, int> &, pair<int, int> &)> cmp = [](auto const &a, auto const &b) { return a.first > b.first; };
    sort(one, one + size_one, cmp);
    sort(two, two + size_two, cmp);

    // cout << "max cap: " << max_cap << endl;

    // cout << "one: ";
    // for (int i = 0; i < size_one; i++)
    // {
    //     cout << one[i].first << " ";
    // }
    // cout << endl;

    // cout << "two: ";
    // for (int i = 0; i < size_two; i++)
    // {
    //     cout << two[i].first << " ";
    // }
    // cout << endl;

    int oi, ti;
    int load = 0;
    vector<int> num_one;
    vector<int> num_two;

    oi = ti = 0;
    while (max_cap > 1 && (oi < size_one || ti < size_two))
    {
        if (!(oi < size_one))
        {
            const auto &v = two[ti++];
            load += v.first;
            max_cap -= 2;
            num_two.push_back(v.second);
        }
        else if (!(ti < size_two))
        {
            const auto &v = one[oi++];
            load += v.first;
            max_cap -= 1;
            num_one.push_back(v.second);
        }
        else if (one[oi].first >= two[ti].first)
        {
            const auto &v = one[oi++];
            load += v.first;
            max_cap -= 1;
            num_one.push_back(v.second);
        }
        else if (oi < size_one - 1 && one[oi].first + one[oi + 1].first > two[ti].first)
        {
            const auto &v1 = one[oi++];
            const auto &v2 = one[oi++];

            load += v1.first + v2.first;
            max_cap -= 2;
            num_one.push_back(v1.second);
            num_one.push_back(v2.second);
        }
        else
        {
            const auto &v = two[ti++];
            load += v.first;
            max_cap -= 2;
            num_two.push_back(v.second);
        }
    }

    if (max_cap == 1 && (oi < size_one || ti < size_two))
    {
        if (!(ti < size_two))
        {
            const auto &v = one[oi];
            load += v.first;
            num_one.push_back(v.second);
        }
        else if (!(oi < size_one))
        {
            if (size_one > 0 && one[oi - 1].first < two[ti].first)
            {
                load += two[ti].first - one[oi - 1].first;
                num_one.pop_back();
                num_two.push_back(two[ti].second);
            }
        }
        else
        {
            if (size_one > 1 && two[ti].first > one[oi].first + one[oi - 1].first)
            {
                load += two[ti].first - one[oi - 1].first;
                num_one.pop_back();
                num_two.push_back(two[ti].second);
            }
            else
            {
                load += one[oi].first;
                num_one.push_back(one[oi].second);
            }
        }
    }

    cout << load << endl;

    // cout << "size " << num_one.size() << endl;
    for (auto const &n : num_one)
    {
        cout << n << ' ';
    }
    for (auto const &n : num_two)
    {
        cout << n << ' ';
    }

    cout << endl;
}
