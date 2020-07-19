#include <iostream>
#include <string>
#include <cctype>
#include <functional>

using namespace std;

int main()
{
    string word;

    cin >> word;

    int low_size = 0;
    for (auto const &ch : word)
    {
        if (islower(ch))
        {
            low_size++;
        }
    }

    function<char(int)> convert_fn;
    if (2 * low_size < word.size())
    {
        convert_fn = [](unsigned char c) { return toupper(c); };
    }
    else
    {
        convert_fn = [](unsigned char c) { return tolower(c); };
    }

    for (auto const &ch : word)
    {
        cout << convert_fn(ch);
    }
    cout << endl;
}