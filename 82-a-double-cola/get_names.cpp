#include <iostream>
#include <cmath>
#include <array>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int q = 5;
    int i = 1;

    while (n > q)
    {
        n -= q;
        i++;
        q *= 2;
    }

    int l = 1 << (i - 1); // same as (int)pow(2, i-1)
    int idx = (int)((n + l - 1) / l) - 1;

    array<string, 5> names = {"Sheldon", "Leonard", "Penny", "Rajesh", "Howard"};

    cout << names[idx] << endl;
}
