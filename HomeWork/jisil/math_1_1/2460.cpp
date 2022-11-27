using namespace std;

#include <iostream>
#include <algorithm>
#include <vector>

int maxPeople = 10000;

struct Train {
    int tmp1, tmp2;
};
vector<Train> numPeople;
int sum, cmp;

int main()
{
    cmp = 0;
    for (int i = 0; i < 10; i++)
    {
        Train tmp;
        cin >> tmp.tmp1 >> tmp.tmp2;
        numPeople.push_back(tmp);
    }

    for (int j = 0; j < 10; j++)
    {
        sum -= numPeople.at(j).tmp1;
        sum += numPeople.at(j).tmp2;
        if (sum > cmp)
        {
            cmp = sum;
        }
    }

    cout << cmp;
}
