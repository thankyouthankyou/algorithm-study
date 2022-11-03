
#include <iostream>
#include <vector>
using namespace std;

vector<int> number;
int M, N;
int cnt, sum;
int main()
{
    cin >> M >> N;
    for (int i = M; i <= N; i++)
    {
        cnt = 0;
        for (int j = 2; j <= i; j++)
        {
            if (i % j == 0)
            {
                cnt++;
            }

            if (cnt > 2)
            {
                break;
            }
        }
        if (cnt == 1)
        {
            number.push_back(i);
            sum += i;
        }
    }
    if (number.empty())
    {
        cout << -1;
    }
    else
    {
        cout << sum << endl;
        cout << number.at(0);
    }
}