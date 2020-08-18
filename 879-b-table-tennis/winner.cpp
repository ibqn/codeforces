#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;

    int power;
    int wins = 0;

    cin >> power;

    int p;
    for (int i = 1; i < n; i++)
    {
        cin >> p;

        if (power > p)
        {
            wins++;
        }
        else
        {
            wins = 1;
            power = p;
        }

        if (wins == k)
        {
            break;
        }
    }

    cout << power << endl;
}
