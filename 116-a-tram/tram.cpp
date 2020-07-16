#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int a, b;
    int flow = 0, capacity = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> a >> b;
        flow += b - a;
        capacity = max(capacity, flow);
    }

    cout << capacity << endl;
}