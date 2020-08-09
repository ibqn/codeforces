#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, t;
    cin >> n >> t;

    vector<int> board;

    for (int i = 0; i < n; i++)
    {
        int p;
        cin >> p;
        board.push_back(p);
    }

    int i = 1;
    while (i < t)
    {
        i += board[i - 1];
    }

    if (i == t)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    cout << endl;
}
