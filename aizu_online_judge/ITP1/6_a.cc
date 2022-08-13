#include <iostream>

using namespace std;

const int N = 1e3 + 10;

int q[N];

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> q[i];
    for (int i = n - 1; i > 0; i--) cout << q[i] << " ";
    cout << q[0] << endl;
    return 0;
}