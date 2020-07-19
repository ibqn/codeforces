#include <iostream>
#include <string>

using namespace std;

int main()
{
    string number;
    cin >> number;

    int count = 0;
    for (auto const &c : number)
    {
        if (c == '4' || c == '7')
        {
            count++;
        }
    }

    cout << ((count == 4 || count == 7) ? "YES" : "NO") << endl;
}