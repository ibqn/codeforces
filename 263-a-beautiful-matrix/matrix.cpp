#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    constexpr int five = 5;
    int x;
    for (int i = 0; i < five * five; i++)
    {
        cin >> x;
        if (x == 1)
        {
            cout << abs(2 - i / five) + abs(2 - i % five) << endl;
            return 0;
        }
    }
}