#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int r;
    int neg = 0;
    int folder = 0;
    vector<int> reports_in_folder = {0};
    for (int i = 0; i < n; i++)
    {
        cin >> r;

        if (r < 0)
        {
            neg++;
        }

        if (neg > 2)
        {
            neg = 1;
            folder++;
            reports_in_folder.push_back(0);
        }

        reports_in_folder[folder]++;
    }

    cout << folder + 1 << endl;
    for (auto const &reports : reports_in_folder)
    {
        cout << reports << " ";
    }
    cout << endl;
}
