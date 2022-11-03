#include <iostream>
#include <list>
#include <cmath>
using namespace std;

int numberK[1000001] = { 0, };

int check[1000001];
int N, K;
int main()
{
    cin >> N >> K;

    for (int i = 2; i <= K; i++)
        numberK[i] = i;

    for (int i = 2; i <= sqrt(K); i++)
    {
        if (numberK[i] == 0)
        {
            continue;
        }
        for (int j = i * i; j <= K; j += i)
        {
            numberK[j] = 0;
        }
    }

    for (int i = N; i <= K; i++)
    {
        if (numberK[i] != 0)
            cout << numberK[i] << '\n';
    }
}
