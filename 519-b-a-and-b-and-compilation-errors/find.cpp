#include <iostream>

using namespace std;

int sum_up(int n)
{
    int sum = 0;

    int v;
    for (int i = 0; i < n; i++)
    {
        cin >> v;
        sum += v;
    }
    return sum;
}

int main()
{
    int n;
    cin >> n;

    int first_sum = sum_up(n);
    int second_sum = sum_up(n - 1);
    int third_sum = sum_up(n - 2);

    cout << first_sum - second_sum << endl
         << second_sum - third_sum << endl;
}
