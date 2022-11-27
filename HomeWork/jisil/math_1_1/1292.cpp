
#include <iostream>
#include <vector>
using namespace std;

int N, K;
int i, j, cnt, sum;
vector<int> number;
int main()
{
    cin >> N >> K;
    i = 1;
    while (i != 1000)
    {
        j = 0;
        while (j != i)
        {
            number.push_back(i);
            j++;
            cnt++;
            if (cnt >= N && cnt <= K)
                sum += i;
            else if (cnt > K)
                break;
        }
        i++;
    }
    cout << sum;
}