#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    string colors = "CYM";
    for (int i = 0; i < n * m; i++)
    {
        char c;
        cin >> c;
        if (string::npos != colors.find(c))
        {
            cout << "#Color" << endl;
            return 0;
        }
    }

    cout << "#Black&White" << endl;
}
