using namespace std;

#include <iostream>
#include <vector>

int main()
{
    int T, res = 0, pos = 0;
    int temp;
    vector<int> N;

    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cin >> temp;
        N.push_back(temp);
    }
    for (int j = 0; j < N.size(); j++)
    {
        int num2 = N.at(j);

        while (1)
        {
            int tmp = num2 % 2;
            
            if (tmp == 1)
            {
                cout << pos << " ";
            }
            num2 /= 2;
            if (num2 == 0)
            {
                break;
            }
            pos++;
        }
        pos = 0;
        cout << endl;
    }
}
