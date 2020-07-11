#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int w;
    cin >> w;

    vector<string> words;

    string word;
    while (w--)
    {
        cin >> word;
        words.push_back(word);
    }

    for (auto const &word : words)
    {
        if (word.size() > 10)
        {
            cout << word[0] << word.size() - 2 << word[word.size() - 1] << endl;
        }
        else
        {
            cout << word << endl;
        }
    }
}