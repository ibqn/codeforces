#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int x, y, z;
    x = y = z = 0;
    for (int i = 0; i < n; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        x += a;
        y += b;
        z += c;
    }

    string answer = (x == 0 && y == 0 && z == 0) ? "YES" : "NO";
    cout << answer << endl;
}
