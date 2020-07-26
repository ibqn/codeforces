#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<pair<string, int>> hist;
    map<string, int> scores;
    for (int i = 0; i < n; i++)
    {
        string name;
        int score;

        cin >> name >> score;
        scores[name] += score;
        hist.push_back(make_pair(name, scores[name]));
    }

    int max_score = -1000;
    for (auto const &it : scores)
    {
        max_score = max(max_score, it.second);
    }

    for (auto const &it : hist)
    {
        if (scores[it.first] == max_score && it.second >= max_score)
        {
            cout << it.first << endl;
            break;
        }
    }
}
