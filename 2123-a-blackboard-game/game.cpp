#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;
        string answer = "alice";

        if (n % 4 == 0)
        {
            answer = "bob";
        }

        cout << answer << endl;
    }
}
