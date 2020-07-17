#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double a, b;
    cin >> a >> b;

    // cout << "a " << a << " b " << b << " log " << log(b / a) << " log 3/2 " << log(3.0 / 2.0) << " result " << log(b / a) / log(3.0 / 2.0) << endl;
    // cout << ceil(log(b / a) / log(3.0 / 2.0) + 0.00001) << endl;
    cout << int(log(b / a) / log(3.0 / 2.0)) + 1 << endl;

    // int result = 0;
    // while (a <= b)
    // {
    //     a *= 3;
    //     b *= 2;
    //     result++;
    // }
    // cout << result << endl;
}
