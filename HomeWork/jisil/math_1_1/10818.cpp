using namespace std;

#include <iostream>
#include <algorithm>
#include <vector>

int N, minNum = -1000000;
int maxNum = 1000000;
int num[1000000];
int cmp1, cmp2, tmp;
int main()
{
    cmp1 = minNum;
    cmp2 = maxNum;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        num[i] = tmp;
    }

    for (int j = 0; j < N; j++)
    {
        if (num[j] <= cmp2)
        {
            cmp2 = num[j];
        }
        if (num[j] >= cmp1)
        {
            cmp1 = num[j];
        }
    }

    cout << cmp2 <<" "<< cmp1;

}
