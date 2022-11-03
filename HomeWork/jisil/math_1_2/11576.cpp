
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int N, K, num;
vector<int> numN, numK;
int TEN;
int main()
{
    cin >> N >> K;
    cin >> num;
    for (int i = 0; i < num; i++)
    {
        int tmp;
        cin >> tmp;
        numN.push_back(tmp);
    }
    for (int i = 0; i < num; i++)
    {
        TEN += pow(N, i) * numN.back();
        numN.pop_back();
    }

    while (TEN != 0)
    {
        numK.push_back(TEN % K);
        TEN /= K;
    }
    int n = numK.size();
    for (int i = 0; i < n; i++)
    {
        cout << numK.back() << " ";
        numK.pop_back();
    }
}