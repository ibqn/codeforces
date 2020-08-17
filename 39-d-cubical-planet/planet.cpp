#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int x1, y1, z1;
    cin >> x1 >> y1 >> z1;

    int x2, y2, z2;
    cin >> x2 >> y2 >> z2;

    bool answer = pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2) < 3;

    cout << (answer ? "YES" : "NO") << endl;
}
