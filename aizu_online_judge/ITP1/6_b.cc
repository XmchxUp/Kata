#include <iostream>
#include <vector>
#include <map>

using namespace std;

const int N = 52;

int main()
{
    int n;
    cin >> n;
    map<std::pair<char, int>, bool> cards;
    for (int i = 0; i < n; i++)
    {
        char c = ' ';
        cin >> c;
        int rank = 0;
        cin >> rank;
        cards[make_pair(c, rank)] = true;
    }
    vector<char> suits = {'S', 'H', 'C', 'D'};
    for (char s : suits)
    {
        for (int i = 1; i <= 13; i++)
        {

            if (cards.find(make_pair(s, i)) == cards.end())
            {
                cout << s << " " << i << endl;
            }
        }
    }
    return 0;
}