#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, k;

    cin >> n >> k;

    string queue;

    cin >> queue;

    while (k--)
    {
        for (int i = 0; i < queue.size() - 1; i++)
        {
            if (queue[i] == 'B' && queue[i + 1] == 'G')
            {
                queue[i] = 'G';
                queue[i + 1] = 'B';
                i++;
            }
        }
    }

    cout << queue << endl;
}