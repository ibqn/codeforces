#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    string s;
    cin >> s;

    vector<char> chars;

    for (auto const &c : s)
    {
        if (c != '+')
        {
            chars.push_back(c);
        }
    }

    sort(chars.begin(), chars.end());

    for (int i = 0; i < chars.size() - 1; i++)
    {
        cout << chars[i] << '+';
    }

    cout << chars[chars.size() - 1] << endl;
}