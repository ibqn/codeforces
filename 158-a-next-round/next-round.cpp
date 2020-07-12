#include <iostream>

using namespace std;

int main()
{
    int n, k;

    cin >> n >> k;

    int res = 0;
    int a;

    for (int i = 0; i < k; i++)
    {
        cin >> a;
        if (a <= 0)
        {
            cout << res << endl;
            return 0;
        }
        res += 1;
    }

    int ak = a;

    for (int i = 0; i < n - k; i++)
    {
        cin >> a;
        if (ak != a)
        {
            break;
        }
        res += 1;
    }

    cout << res << endl;
}