#include <iostream>

using namespace std;

int main()
{
    int n;

    cin >> n;

    int result = 0;

    int step = 5;
    int size;
    while (step > 0)
    {
        // cout << "step " << step << endl;
        size = n / step;
        result += size;
        if (n % step == 0)
        {
            break;
        }

        n -= size * step;
        step--;
    }

    cout << result << endl;
}