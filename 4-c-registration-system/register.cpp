#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main()
{
    unordered_map<string, int> um;

    int n;

    cin >> n;

    string name;
    for (int i = 0; i < n; i++)
    {
        cin >> name;

        auto search = um.find(name);
        if (search != um.end())
        {
            cout << name << search->second << endl;
            search->second = search->second + 1;
        }
        else
        {
            cout << "OK" << endl;
            um.insert({name, 1});
        }
    }
}