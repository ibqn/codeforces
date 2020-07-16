#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    char last_ch = 'F';
    int count = 0;
    string sequence;
    cin >> sequence;

    for (auto const &ch : sequence)
    {
        if (ch == last_ch)
        {
            count++;
        }
        last_ch = ch;
    }

    cout << count << endl;
}