#include <iostream>
#include <unordered_map>

using namespace std;

int main()
{
    string sequence;

    cin >> sequence;

    unordered_map<char, int> map;
    for (auto const &ch : sequence)
    {
        map[ch]++;
    }

    cout << ((map.size() % 2 == 0) ? "CHAT WITH HER!" : "IGNORE HIM!") << endl;
    // int count = 0;
    // for (auto const &it : map)
    // {
    //     count++;
    // }
    // cout << ((count % 2 == 0) ? "CHAT WITH HER!" : "IGNORE HIM!") << endl;
}