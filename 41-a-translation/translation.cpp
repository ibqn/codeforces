#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string word1, word2;

    cin >> word1 >> word2;

    reverse(word2.begin(), word2.end());

    cout << ((word1 == word2) ? "YES" : "NO") << endl;
}
