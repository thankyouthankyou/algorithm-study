
#include <iostream>
#include <vector>
using namespace std;

int N, cnt, result;
vector<int> vec;
int main()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int tmp;
        cin >> tmp;
        vec.push_back(tmp);
    }

    for (int a : vec)
    {
        cnt = 0;
        for (int i = 2; i < 1000; i++)
        {
            if ((a % i == 0))
            {
                cnt++;
            }
            if (cnt > 2)
                break;
        }
        if (cnt == 1)
        {
            result++;
        }
    }
    cout << result << endl;
}