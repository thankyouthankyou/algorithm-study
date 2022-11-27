using namespace std;

#include <iostream>
#include <list>

list<int> smallPeople;
int sum, k;

list<int> Calculate(list<int> sList)
{
    int s;
    s = sum;
    list<int>::iterator iter1;
    list<int>::iterator iter2;

    for (iter1 = sList.begin(); iter1 != sList.end(); ++iter1)
    {
        for (iter2 = sList.begin(); iter2 != sList.end(); ++iter2)
        {
            if (iter1 == iter2)
            {
                continue;
            }
            s -= (*iter1 + *iter2);
            if (s == 100)
            {
                sList.erase(iter1);
                sList.erase(iter2);
                return sList;
            }
            s += (*iter1 + *iter2);
        }
    }
}
int main()
{
    for (int i = 0; i < 9; i++)
    {
        int tmp;
        cin >> tmp;
        smallPeople.push_back(tmp);
    }
    for (int a : smallPeople)
    {
        sum += a;
    }
    list<int> result = Calculate(smallPeople);
    result.sort();
    for (int r : result)
    {
        cout << r << endl;
    }
}
