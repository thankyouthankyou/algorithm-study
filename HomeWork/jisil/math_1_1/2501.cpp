using namespace std;

#include <iostream>
#include <vector>

int main()
{
    int N, K, res = 0, nK = 0;
    vector<int> resNum;
    cin >> N >> K;

    for (int i = 1; i <= 10000; i++)
    {
        if (N % i == 0)
        {
            resNum.push_back(i);
            res++;
            if (res == K)
            {
                nK = resNum.at(res-1);
                break;
            }
            else if (res > K)
            {
                nK = 0;
                break;
            }
        }
    }
    cout << nK;
}
