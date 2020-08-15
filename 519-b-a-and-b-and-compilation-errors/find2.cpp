#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int find_missing(vector<int> &orig, vector<int> &ref)
{
    int result = orig.back();

    for (int i = 0; i < ref.size(); i++)
    {
        if (orig[i] != ref[i])
        {
            return orig[i];
        }
    }

    return result;
}

void fill_list(vector<int> &vec, int size)
{
    int v;
    for (int i = 0; i < size; i++)
    {
        cin >> v;
        vec.push_back(v);
    }
}

int main()
{
    int n;
    cin >> n;

    vector<int> first;
    vector<int> second;
    vector<int> third;

    fill_list(first, n);
    fill_list(second, n - 1);
    fill_list(third, n - 2);

    sort(first.begin(), first.end());
    sort(second.begin(), second.end());
    sort(third.begin(), third.end());

    cout << find_missing(first, second) << endl
         << find_missing(second, third) << endl;
}
