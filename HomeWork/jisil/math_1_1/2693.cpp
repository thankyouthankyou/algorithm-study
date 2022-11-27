
#include <iostream>
#include <list>
#include <vector>
using namespace std;

int N;
list<list<int>> listAll;
list<int>::iterator iter;
int main()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        list<int> li;

        for (int j = 0; j < 10; j++)
        {
            int tmp;
            cin >> tmp;
            li.push_back(tmp);
        }
        listAll.push_back(li);
    }
    for (list<int> a : listAll)
    {
        a.sort();
        a.pop_back();
        a.pop_back();
        cout << a.back() << endl;
    }
}