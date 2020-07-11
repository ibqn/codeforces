#include <iostream>

using namespace std;

int main()
{
    int w;
    cin >> w;
    string out = (w % 2 == 0 && w > 2) ? "YES" : "NO";
    cout << out << endl;
}