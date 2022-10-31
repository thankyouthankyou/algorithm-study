using namespace std;

#include <iostream>

int n;
int fibo[20] = { 0, };
int main()
{
    fibo[0] = 0;
    fibo[1] = 1;
    cin >> n;
    for (int i = 2; i <= n; i++)
    {
        fibo[i] = fibo[i-2] + fibo[i-1];
    }
    cout << fibo[n];
}
