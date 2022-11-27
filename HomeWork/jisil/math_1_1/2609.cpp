
#include <iostream>
using namespace std;

long long N, K;
long long nGcd = 2, nLcm = 0;

int gcd(long long a, long long b)
{
    long long tmp;
    while (b != 0)
    {
        tmp = a;
        a = b;
        b = tmp % b;
    }
    return a;
}

int main()
{
    cin >> N >> K;
    nGcd = gcd(N, K);
    nLcm = N * K / nGcd;

    cout << nGcd << endl << nLcm;
}
