#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

int main()
{
    constexpr int size = 4;
    array<int, size> points;

    for (auto &it : points)
    {
        cin >> it;
    }

    sort(points.begin(), points.end());

    bool segment = false;
    for (int i = 0; i < size - 2; i++)
    {
        if (points[i] + points[i + 1] > points[i + 2])
        {
            cout << "TRIANGLE" << endl;
            return 0;
        }
        else if (points[i] + points[i + 1] == points[i + 2])
        {
            segment = true;
        }
    }

    if (segment)
    {
        cout << "SEGMENT" << endl;
    }
    else
    {
        cout << "IMPOSSIBLE" << endl;
    }
}
