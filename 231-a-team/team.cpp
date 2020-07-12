#include <iostream>

using namespace std;

int main()
{
    int w;
    cin >> w;

    int res = 0;
    int a, b, c;
    for (int i = 0; i < w; i++)
    {
        cin >> a >> b >> c;
        res += (a + b + c > 1) ? 1 : 0;
    }

    cout << res << endl;
}