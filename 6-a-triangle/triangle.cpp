#include <iostream>

using namespace std;

int main()
{
    constexpr int size = 4;
    int points[size];

    for (int i = 0; i < size; i++)
    {
        cin >> points[i];
    }

    int sum, diff;
    bool segment = false;
    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            sum = points[i] + points[j];
            diff = abs(points[i] - points[j]);
            for (int k = 0; k < size; k++)
            {
                if (i != k && j != k)
                {
                    if (points[k] < sum && points[k] > diff)
                    {
                        cout << "TRIANGLE" << endl;
                        return 0;
                    }
                    else if (points[k] == sum)
                    {
                        segment = true;
                    }
                }
            }
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
