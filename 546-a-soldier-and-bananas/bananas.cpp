#include <iostream>

using namespace std;

int main()
{
    int k, n, w;

    cin >> k >> n >> w;

    cout << max(w * (w + 1) / 2 * k - n, 0) << endl;
}