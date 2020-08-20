#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, length;

    cin >> n >> length;

    vector<int> positions;

    for (int i = 0; i < n; i++)
    {
        int p;
        cin >> p;

        positions.push_back(p);
    }

    sort(positions.begin(), positions.end());

    double radius = max(positions[0], length - positions[n - 1]);

    for (int i = 1; i < n; i++)
    {
        radius = max(radius, (positions[i] - positions[i - 1]) / 2.0);
    }

    cout << std::fixed << radius << endl;
}
