#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

int main()
{
    int d;
    int sum_time;

    cin >> d >> sum_time;

    array<int, 30> min_time, max_time, schedule;
    int min = 0, max = 0;

    for (int i = 0; i < d; i++)
    {
        cin >> min_time[i] >> max_time[i];
        min += min_time[i];
        max += max_time[i];
        schedule[i] = min_time[i];
    }

    if (min > sum_time || max < sum_time)
    {
        cout << "NO" << endl;
        return 0;
    }

    cout << "YES" << endl;

    sum_time -= min;
    int diff;
    for (int i = 0; i < d && sum_time; i++)
    {
        // cout << ".";
        diff = std::min(sum_time, max_time[i] - min_time[i]);
        sum_time -= diff;
        schedule[i] += diff;
    }

    for (int i = 0; i < d; i++)
    {
        cout << schedule[i] << " ";
    }

    cout << endl;
}