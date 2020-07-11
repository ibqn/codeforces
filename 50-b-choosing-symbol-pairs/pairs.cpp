#include <iostream>
#include <map>

using namespace std;

int main()
{
    string word;
    cin >> word;

    map<char, unsigned long long> counts;

    for (auto const &letter : word)
    {
        counts[letter]++;
        // auto it = counts.find(letter);
        // if (it != counts.end())
        // {
        //     it->second = it->second + 1;
        // }
        // else
        // {
        //     counts.insert({letter, 1});
        // }
    }

    unsigned long long result = 0;
    for (auto const &cnt : counts)
    {
        result += cnt.second * cnt.second;
    }

    cout << result << endl;
}