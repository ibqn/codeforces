#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int result = 0;
    for (int i = 0; i < n; i++)
    {
        string statement;
        cin >> statement;
        if (statement.compare("X++") == 0 || statement.compare("++X") == 0)
        {
            result++;
        }
        else //if (statement.compare("X--") || statement.compare("--X"))
        {
            result--;
        }
    }
    cout << result << endl;
}